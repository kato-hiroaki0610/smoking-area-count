import json
import pathlib
from typing import List

import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from pydantic.fields import Required
from starlette.responses import JSONResponse

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
    p_dir = pathlib.Path('.')
    setting_file_name = p_dir / SETTING_FILE_DIR / SETTING_FILE_NAME
    log.logger.debug(setting_file_name)

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

    # 存在部屋をURLに打ち込んだ場合
    if 'area' not in target_room.keys():
        error_result = {'detail': [{'msg': 'room not found'}]}
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                            content=error_result)

    json_creater = CreateJson(target_room)
    json_creater.execute_create()
    created_json = jsonable_encoder(json_creater.get_created_json())

    log.logger.debug(created_json)

    # return {'specified_room_status': created_json}
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={'room_status': created_json})


@app.get('/multiple')
async def multiple_room(room: List[str] = Query(Required)) -> json:
    """指定した複数の部屋の情報を取得する

    Args:
        rooms (List[str]): 部屋名

    Returns:
        json: 指定された部屋情報、
              存在しない部屋がしていされた場合は空のdictを返す
    """
    detect_field_num_key = 'detect_field_num'
    setting = read_toml()

    target_room = {}
    target_room[detect_field_num_key] = setting[detect_field_num_key]

    target_room['area'] = []

    for current_room in room:
        for area in setting['area']:
            if area['場所'] == current_room:
                target_room['area'].append(area)
                break

    # 存在部屋をURLに打ち込んだ場合
    if len(target_room['area']) == 0:
        error_result = {'detail': [{'msg': 'room not found'}]}
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                            content=error_result)

    json_creater = CreateJson(target_room)
    json_creater.execute_create()
    created_json = jsonable_encoder(json_creater.get_created_json())

    log.logger.debug(created_json)

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={'room_status': created_json})


if __name__ == '__main__':
    uvicorn.run('fast_api:app', reload=False)
