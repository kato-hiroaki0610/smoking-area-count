"""JSONを作成するクラス"""

import json
from typing import Dict, List


class CreateJson:
    """JSONを作成するクラス"""

    def __init__(self, rows: List[List], settings: Dict) -> None:
        """コンストラクタ

        Args:
            rows(List[List]): 読み込んだCSV
                                [[1行目], [2行目], ..., [n行目]]の形になっている
            settings(Dict): 読み込んだToml
        """
        self._last_row = self.get_last_row(rows)
        self._setting = settings
        self._created_json = ''

    def get_last_row(self, rows: List[List]) -> List:
        """読み込んだCSVから最終行を取得する

        Args:
            rows[List[List]]: 読み込んだCSV
                                [[1行目], [2行目], ..., [n行目]]の形になっている
        Return:
            読み込んだCSVから最終行のみを返す
        """
        return rows[-1]

    def get_detect_column(self) -> int:
        """最終行のから検知数を取得する

        Return:
            検知数
        """
        detect_num = self._setting['detect_field_num']
        count = self._last_row[detect_num]

        if type(count) == int:
            return count
        else:
            return int(count)

    def is_capacity_over(self, count: int) -> bool:
        """喫煙室が定員上限か判定する

        Args:
            count(int): 検知数
        Return:
            定員上限か
        """
        # FIXME とりあえず5階を指定
        capacity_limit = self._setting['capacity_limit']['5F']

        if type(capacity_limit) != int:
            capacity_limit = int(capacity_limit)

        if count <= capacity_limit:
            return True
        else:
            return False

    def execute_create(self) -> None:
        """リストと辞書からJsonを作成する"""
        json_dict = {}

        json_dict['階数'] = 'todo'
        detect_num = self.get_detect_column()
        json_dict['利用者数'] = detect_num
        json_dict['待ち人数'] = 'todo'
        json_dict['上限超え'] = self.is_capacity_over(detect_num)

        self._created_json = json.dumps(json_dict)

    def get_created_json(self) -> json:
        """作成したJsonを取得する

        Return:
            作成したJson
        """
        return self._created_json
