"""喫煙室利用者数が書かれたCSVファイルの処理を行うモジュール"""

import logging

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForCSV(FileReader):
    """人名が書かれたファイルの処理を行うクラス"""
    def set_input_file(self, file_path):
        """コンストラクタ

        Args:
            file_path(str): 入力ファイルパス
        """
        self.file_path = file_path

    def parse_file(self):
        """ファイルから人数を取得する

        Return
            人数
        """
        # TODO    ログ

        # 最終行を取得する
        try:
            with open(self.file_path) as f:
                last_line = [line for line in f.readlines()][-1]
        except IndexError:
            # ログが一行もない場合
            count = 0
            return count

        try:
            count = int(last_line.split(',')[-1])
        except ValueError:
            # 検知人数が入っていない場合
            count = 0

        return count
