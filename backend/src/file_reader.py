"""ファイルリーダークラスの親モジュール"""

from abc import ABCMeta, abstractmethod


class FileReader(metaclass=ABCMeta):
    """ファイルリーダークラスの親クラス"""

    def __init__(self):
        """コンストラクタ"""
        self._file_path = ''
        self._contents = ''

    @abstractmethod
    def set_file_path(self, file_path):
        """フィールドにファイルのパスをセットする

        Args:
            file_path(str): ファイルのパス
        """
        raise NotImplementedError()

    @abstractmethod
    def load_file(self):
        """ファイルを読み込む"""
        raise NotImplementedError()

    @abstractmethod
    def get_contents(self):
        """読み込んだファイルを取得する

        Return ファイル内容
        """
        raise NotImplementedError()
