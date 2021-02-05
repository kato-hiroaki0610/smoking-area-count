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
        self._last_row = ''
        self._setting = ''
        self._created_json = ''

    def __get_last_row(rows: List[List]) -> List:
        """読み込んだCSVから最終行を取得する

        Args:
            rows[List[List]]: 読み込んだCSV
                                [[1行目], [2行目], ..., [n行目]]の形になっている
        Return:
            読み込んだCSVから最終行のみを返す
        """
        pass

    def __get_detect_column(column_num: int) -> int:
        """最終行のから検知数を取得する

        Args:
            column_num(int): CSVの検知数が含まれるカラム番号
        Return:
            検知数
        """
        pass

    def __is_capacity_over(capacity: int) -> bool:
        """喫煙室が定員上限か判定する

        Args:
            capacity(int): 定員上限
        Return:
            定員上限か
        """
        pass

    def execute_create() -> None:
        """リストと辞書からJsonを作成する"""
        pass

    def get_created_json() -> json:
        """作成したJsonを取得する

        Return:
            作成したJson
        """
        pass
