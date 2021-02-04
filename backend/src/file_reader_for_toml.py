"""Tomlファイルリーダー モジュール"""

import logging

import toml

from file_reader import FileReader

logger = logging.getLogger(__name__)


class FileReaderForToml(FileReader):
    """Tomlファイルリーダー クラス"""

    def set_file_path(self, file_path):
        """フィールドにtomlファイルのパスをセットする

        Args:
            file_path(str): Tomlファイルのパス
        """
        self.file_path = file_path

    def load_file(self):
        """Tomlファイルに書かれているパラメーターを解析する

        Return パラメーターの辞書
        """
        try:
            with open(self.file_path, encoding='utf8') as f:
                toml_file = toml.load(f)

                self._contents = toml_file

            return toml_file
        except FileNotFoundError:
            error_value = f'{self.file_path}が見つかりませんでした'
            raise FileNotFoundError(error_value)

    def get_contents(self):
        return self._contents
