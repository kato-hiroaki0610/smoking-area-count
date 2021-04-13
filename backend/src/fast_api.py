import json
import pathlib
import sys
import urllib.parse
from typing import List

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from pydantic.fields import Required
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from create_json import CreateJson
from file_reader_for_toml import FileReaderForToml
from logger import Log

SETTING_FILE_DIR = 'setting'
SETTING_FILE_NAME = 'setting.toml'


app = FastAPI()

# CORS対策
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


def get_frontend_path(path) -> str:
    """Webディレクトリのパスを取得する関数
    Pyinstallerでパッケージングしたexeを実行するとTempフォルダに一時ファイルが展開される
    展開先のパスは`sys._MEIPASS`で取得ができる

    Args:
        path(str): 取得するパス

    Returns:
        str: 取得したパス
    """
    if hasattr(sys, '_MEIPASS'):
        return pathlib.Path(sys._MEIPASS) / path
    return pathlib.Path('.') / path


# ./webディレクトリ以下のファイルを静的ファイルとして指定
# html=Trueを指定することにより、/webににアクセスすることでindex.htmlに自動的にアクセスするようにする
web_directory = get_frontend_path('web')
app.mount('/web',
          StaticFiles(directory=web_directory, html=True),
          name='web')

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


@app.get('/select')
async def redict_view(request: Request) -> RedirectResponse:
    """HTMLにリダイレクトを行う

    Args:
        request(Request): Request

    Returns:
        RedirectResponse: RedirectResponse
    """
    index = 'web/index{0}.html'
    # %エンコーディングされているのででコードを行う
    room = urllib.parse.unquote(str(request.query_params))

    # QueryParameterが存在しなければindex.htmlを返す
    if not room:
        return RedirectResponse(index.format(''))

    # QueryParameterの&区切りのリストを作成する
    rooms_tmp = room.split('&')
    # 'room=n階'の'n階'部屋のみを格納したリスト
    request_rooms = [r.split('=')[-1] for r in rooms_tmp]

    if len(request_rooms) > 0:

        setting = read_toml()
        exists_rooms = [s['場所'] for s in setting['area']]

        # 'room=11階&room=9階'のようなパラメーターの場合でもexists_roomsに格納されている順番に並べ替える
        view_room = [r for r in exists_rooms if r in request_rooms]
        # 'index_n階.html' 'index_n階_m階.html' htmlファイル名を表す文字列を作成する
        html_filename = index.format(''.join(['_' + r for r in view_room]))
    else:
        return RedirectResponse(index.format(''))

    return RedirectResponse(html_filename)


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
