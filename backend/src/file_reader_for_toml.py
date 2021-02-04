"""Tomlファイルリーダー モジュール"""

import logging

import toml

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForToml(FileReader):
    """設定が記載されたTomlファイルの処理を行うクラス"""

    def set_file_path(self, file_path):
        """フィールドにtomlファイルのパスをセットする

        Args:
            file_path(str): Tomlファイルのパス
        """
        self.file_path = file_path

    def load_file(self):
        """Tomlファイルを読み込む"""
        try:
            with open(self.file_path, encoding='utf8') as f:
                toml_file = toml.load(f)

                self._contents = toml_file
        except FileNotFoundError:
            error_value = f'{self.file_path}が見つかりませんでした'
            raise FileNotFoundError(error_value)

    def get_contents(self):
        """読み込んだTomlを返す

        Return
            読み込んだToml
        """
        return self._contents
