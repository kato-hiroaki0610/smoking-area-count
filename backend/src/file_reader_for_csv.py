"""喫煙室利用者数が書かれたCSVファイルの処理を行うモジュール"""

import csv
import logging

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForCSV(FileReader):
    """喫煙室利用者数が書かれたファイルの処理を行うクラス"""

    def set_file_path(self, file_path):
        """フィールドにcsvファイルのパスをセットする

        Args:
            file_path(str): 入力ファイルパス
        """
        self.file_path = file_path

    def load_file(self):
        """CSVを読み込む"""
        # TODO    ログ
        #         CSVが見つからなかった場合
        # 最終行の検知数を取得する
        with open(self.file_path, 'r', encoding='utf8') as f:
            reader = csv.reader(f)

            # iteratorをリストに変換する
            rows = [r for r in reader]

            self._contents = rows

    def get_contents(self):
        """読み込んだCSVを返す

        Return
            読み込んだCSV
        """
        return self._contents
