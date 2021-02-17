"""Loggerを定義するモジュール"""

import logging
import os
from datetime import datetime


class Log:
    """Loggerを定義するクラス"""
    def __init__(self):
        """コンストラクタ"""
        self.logger = None

    def set_logger(self):
        """Loggerを定義するメソッド"""
        logger = logging.getLogger(__name__)

        handlers = []

        log_directory = 'log'
        if not os.path.isdir(log_directory):
            os.mkdir(log_directory)

        timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
        log_filename = os.path.join(log_directory, timestamp + '.log')

        file_handler = logging.FileHandler(log_filename, 'a')
        # handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
        file_handler.setLevel(logging.DEBUG)

        handlers.append(file_handler)

        stream_handler = logging.StreamHandler()

        # handlerのログレベル設定(ハンドラが出力するエラーメッセージのレベル)
        stream_handler.setLevel(logging.INFO)

        handlers.append(stream_handler)

        # Debug用ログ
        log_format = '%(asctime)s %(levelname)-8s' + \
                     '%(module)-18s %(funcName)-10s' + \
                     '%(lineno)4s: %(message)s'

        # log_format = '%(asctime)s : %(message)s'

        logging.basicConfig(handlers=handlers,
                            level=logging.DEBUG,
                            format=log_format)

        self.logger = logger
