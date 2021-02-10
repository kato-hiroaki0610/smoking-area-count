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

    def get_last_row(self, file_name_path: str) -> List or None:
        """CSVを読み込み最終行を取得する

        Args:
            file_name(str): 読み込むCSVのファイルネームパス
        Return:
            読み込んだCSVから最終行のみを返す
        """
        reader = csv_reader()
        reader.set_file_path(file_name_path)
        reader.load_file()
        rows = reader.get_contents()

        if rows is None:
            return None

        return rows[-1]

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
            count(int): 検知数
        Return:
            定員上限か
        """
        capacity_limit = setting['定員上限']

        if type(capacity_limit) != int:
            capacity_limit = int(capacity_limit)

        if capacity_limit >= count:
            return False
        else:
            return True

    def execute_create(self) -> None:
        """リストと辞書からJsonを作成する"""
        json_dict = []
        logger.debug(f'setting: {self._setting}')

        for setting_area in self._setting['area']:
            tmp_json = {}
            current_area = setting_area['場所']
            tmp_json['階数'] = current_area

            # 利用者の最終行を取得する
            last_user_row = self.get_last_row(setting_area['利用者'])
            if last_user_row is not None:
                user_detect_num = self.get_detect_column(last_user_row)
                tmp_json['利用者数'] = user_detect_num

                tmp_json['上限超え'] = self.is_capacity_over(
                    setting_area, user_detect_num)
            else:
                tmp_json['利用者数'] = ''
                tmp_json['上限超え'] = ''

            # 待ち人数の最終行を取得する
            last_wait_user_row = self.get_last_row(setting_area['待ち人数'])
            if last_wait_user_row is not None:
                wait_user_detect_num = self.get_detect_column(
                    last_wait_user_row)
                tmp_json['待ち人数'] = wait_user_detect_num
            else:
                tmp_json['待ち人数'] = ''

            json_dict.append(tmp_json)

        # ensure_ascii=FalseでUnicodeを出力しないようにする
        self._created_json = json.dumps(json_dict, ensure_ascii=False)
        logger.debug(f'created: {self._created_json}')

    def get_created_json(self) -> json:
        """作成したJsonを取得する

        Return:
            作成したJson
        """
        return self._created_json
