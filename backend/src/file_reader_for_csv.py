"""喫煙室利用者数が書かれたCSVファイルの処理を行うモジュール"""

import csv
import logging

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForCSV(FileReader):
    """喫煙室利用者数が書かれたファイルの処理を行うクラス"""
    def set_input_file(self, file_path):
        """コンストラクタ

        Args:
            file_path(str): 入力ファイルパス
        """
        self.file_path = file_path
        # 検知数が格納されているカラムのヘッダー名
        self.detect_field_name = ' 検知数'

    def parse_file(self):
        """ファイルから人数を取得する

        Return
            人数
        """
        # TODO    ログ
        #         CSVが見つからなかった場合
        # 最終行の検知数を取得する
        with open(self.file_path, 'r', encoding='utf8') as f:
            reader = csv.DictReader(f)

            # ログが1行（ヘッダーのみ）の場合
            if reader.line_num == 1:
                return 0

            # iteratorをリストに変換する
            rows = [r for r in reader]

            # 最終行を取得
            last_line = rows[-1]

            # 検知数を取得
            count = last_line[self.detect_field_name]

        return count
