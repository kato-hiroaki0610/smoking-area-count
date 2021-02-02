"""Tomlファイルリーダー モジュール"""

import logging

import toml

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForToml(FileReader):
    """Tomlファイルリーダー クラス"""
    def set_input_file(self, file_path):
        """フィールドにtomlファイルのパスをセットする

        Args:
            file_path(str): Tomlファイルのパス
        """
        self.file_path = file_path

    def parse_file(self):
        """Tomlファイルに書かれているパラメーターを解析する

        Return パラメーターの辞書
        """
        try:
            with open(self.file_path, encoding='utf8') as f:
                toml_file = toml.load(f)

            return toml_file
        except FileNotFoundError:
            error_value = f'{self.file_path}が見つかりませんでした'
            raise FileNotFoundError(error_value)
