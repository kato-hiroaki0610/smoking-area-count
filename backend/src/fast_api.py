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


@app.get('/')
def main():
    log.set_logger()
    setting_file_name = os.path.join(os.path.dirname(__file__),
                                     SETTING_FILE_DIR, SETTING_FILE_NAME)
    log.logger.info(setting_file_name)

    toml_reader = FileReaderForToml()
    toml_reader.set_file_path(setting_file_name)
    toml_reader.load_file()
    toml = toml_reader.get_contents()

    json_creater = CreateJson(toml)
    json_creater.execute_create()
    created_json = jsonable_encoder(json_creater.get_created_json())

    log.logger.debug(created_json)

    return {'room_status': created_json}


@app.post('/specified')
def specified_room():
    pass
