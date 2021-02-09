"""喫煙室利用者数が書かれたCSVファイルの処理を行うモジュール"""

import csv
import logging
import os
from typing import List

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForCSV(FileReader):
    """喫煙室利用者数が書かれたファイルの処理を行うクラス"""
    def set_file_path(self, file_path: str) -> None:
        """フィールドにcsvファイルのパスをセットする

        Args:
            file_path(str): 入力ファイルパス
        """
        self._file_path = file_path

    def load_file(self) -> None:
        """CSVを読み込む"""
        # TODO    ログ
        # ファイルパスに何も格納されていない場足
        # CSVファイルが見つからなかった場合
        if self._file_path == '' or not os.path.exists(self._file_path):
            self._contents = None
            return

        try:
            with open(self._file_path, 'r', encoding='utf8') as f:
                reader = csv.reader(f)

                # iteratorをリストに変換する
                rows = [r for r in reader]

                self._contents = rows
        except FileNotFoundError:
            error_value = f'{self._file_path}が見つかりませんでした'
            raise FileNotFoundError(error_value)

    def get_contents(self) -> List[List]:
        """読み込んだCSVを返す

        Return
            読み込んだCSV
        """
        return self._contents
