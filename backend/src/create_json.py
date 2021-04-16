"""JSONを作成するクラス"""

import json
import logging
from typing import Dict, List

from file_reader_for_csv import FileReaderForCSV as csv_reader

logger = logging.getLogger(__name__)


class CreateJson:
    """JSONを作成するクラス"""
    def __init__(self, settings: Dict) -> None:
        """コンストラクタ

        Args:
            settings(Dict): 読み込んだToml
        """
        self._setting = settings
        self._created_json = ''

    def get_last_row(self, file_path: str) -> List or None:
        """CSVを読み込み最終行を取得する

        Args:
            file_path(str): 読み込むCSVのファイルパス
        Return:
            読み込んだCSVから最終行のみを返す
        """
        try:
            reader = csv_reader()
            reader.set_file_path(file_path)
            reader.load_file()
            rows = reader.get_contents()

            # ファイルは存在するが空の場合
            if rows is None:
                return None

            return rows[-1]
        except FileNotFoundError:
            return None
        except FileExistsError:
            return None

    def get_detect_column(self, last_row: List) -> int:
        """最終行から検知数を取得する

        Args:
            last_row(List): 最終行

        Return:
            検知数
        """
        detect_num = self._setting['detect_field_num']
        count = last_row[detect_num]

        if type(count) == int:
            return count
        else:
            return int(count)

    def is_capacity_over(self, setting: dict, count: int) -> bool:
        """喫煙室が定員上限か判定する
            Trueなら定員上限、Falseなら空きがある

        Args:
            setting(dict): 設定ファイルを読み込んだ辞書
            count(int): 検知数
        Return:
            定員上限か
        """
        if type(setting['定員上限']) != int:
            capacity_limit = int(setting['定員上限'])
        else:
            capacity_limit = setting['定員上限']

        if type(count) != int:
            detect_num = int(count)
        else:
            detect_num = count

        if capacity_limit >= detect_num:
            return False
        else:
            return True

    def execute_create(self) -> None:
        """リストと辞書からjsonを作成する"""
        json_dict = []
        logger.debug(f'setting: {self._setting}')

        for setting_area in self._setting['area']:
            tmp_json = {}
            current_area = setting_area['場所']
            tmp_json['room'] = current_area

            # 利用者の最終行を取得する
            last_user_row = self.get_last_row(setting_area['利用者'])
            if last_user_row is not None:
                user_detect_num = self.get_detect_column(last_user_row)
                tmp_json['use'] = user_detect_num
                tmp_json['is_limit'] = self.is_capacity_over(
                    setting_area, user_detect_num)
            else:
                tmp_json['use'] = ''
                tmp_json['is_limit'] = ''

            # 待ち人数の最終行を取得する
            last_wait_user_row = self.get_last_row(setting_area['待ち人数'])
            if last_wait_user_row is not None:
                wait_user_detect_num = self.get_detect_column(
                    last_wait_user_row)
                tmp_json['wait'] = wait_user_detect_num
            else:
                tmp_json['wait'] = ''

            tmp_json['limit'] = setting_area['定員上限']

            json_dict.append(tmp_json)

        self._created_json = json_dict
        logger.debug(f'created: {self._created_json}')

    def get_created_json(self) -> json:
        """作成したJsonを取得する

        Return:
            作成したJson
        """
        return self._created_json
