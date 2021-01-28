"""ファイルリーダークラスの親モジュール"""

from abc import ABCMeta, abstractmethod


class FileReader(metaclass=ABCMeta):
    """ファイルリーダークラスの親クラス"""
    @abstractmethod
    def set_input_file(self, file_path):
        """フィールドにファイルのパスをセットする

        Args:
            file_path(str): ファイルのパス
        """
        raise NotImplementedError()

    @abstractmethod
    def parse_file(self):
        """ファイルに書かれている内容を解析する

        Return 解析結果
        """
        raise NotImplementedError()
