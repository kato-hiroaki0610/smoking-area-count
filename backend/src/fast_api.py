import json
import os

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from create_json import CreateJson
from file_reader_for_toml import FileReaderForToml
from logger import Log

SETTING_FILE_DIR = 'setting'
SETTING_FILE_NAME = 'setting.toml'

app = FastAPI()
log = Log()
log.set_logger()


def read_toml() -> dict:
    """設定ファイルを読み込む関数

    Returns:
        dict: 読み込んだ設定ファイル
    """
    setting_file_name = os.path.join(os.path.dirname(__file__),
                                     SETTING_FILE_DIR, SETTING_FILE_NAME)
    log.logger.info(setting_file_name)

    try:
        toml_reader = FileReaderForToml()
        toml_reader.set_file_path(setting_file_name)
        toml_reader.load_file()

        return toml_reader.get_contents()
    except FileNotFoundError:
        return


@app.get('/')
async def main() -> json:
    """fast apiのエントリーポイント
    設定ファイルに基づきログファイルから部屋状況を取得する

    Returns:
        json: 設定ファイルに記載された部屋情報
    """
    setting = read_toml()

    json_creater = CreateJson(setting)
    json_creater.execute_create()
    created_json = jsonable_encoder(json_creater.get_created_json())
    log.logger.debug(created_json)

    return {'room_status': created_json}


@app.get('/specified')
async def specified_room(room: str) -> json:
    """指定した一つの部屋の情報を取得する

    Args:
        room (str): 部屋名

    Returns:
        json: 指定された部屋情報、
              存在しない部屋がしていされた場合は空のdictを返す
    """
    detect_field_num_key = 'detect_field_num'
    setting = read_toml()

    target_room = {}
    target_room[detect_field_num_key] = setting[detect_field_num_key]

    for area in setting['area']:
        if area['場所'] == room:
            # 処理の共通化のため、areaはリストで格納された辞書とする
            target_room['area'] = [area]
            break

    if 'area' not in target_room.keys():
        return {'specified_room_status': {}}

    json_creater = CreateJson(target_room)
    json_creater.execute_create()
    created_json = jsonable_encoder(json_creater.get_created_json())

    log.logger.debug(created_json)

    return {'specified_room_status': created_json}
