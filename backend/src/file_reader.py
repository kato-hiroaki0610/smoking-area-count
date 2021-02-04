"""ファイルリーダークラスの親モジュール"""

from abc import ABCMeta, abstractmethod


class FileReader(metaclass=ABCMeta):
    """ファイルリーダークラスの親クラス"""

    @abstractmethod
    def set_file_path(self, file_path):
        """フィールドにファイルのパスをセットする

        Args:
            file_path(str): ファイルのパス
        """
        raise NotImplementedError()

    @abstractmethod
    def load_file(self):
        """ファイルに書かれている内容を解析する

        Return 解析結果
        """
        raise NotImplementedError()
