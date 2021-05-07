import csv
import time

import pytest  # noqa
import toml
from selenium import webdriver


class TestSmokingAreaCount(object):
    def setup_method(self):
        # Selenium Server に接続する
        self.driver = webdriver.Chrome()
        # Selenium 経由でブラウザを操作する
        self.driver.get('http://localhost:8000/web/index.html')
        # time.sleep(5)
        print(self.driver.current_url)

    def open_csv(self, file_path):
        """CSVを開く"""
        with open(file_path, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            # iteratorをリストに変換する
            rows = [r for r in reader]

        return rows

    def open_toml(self, file_path):
        """tomlを開く"""
        with open(self._file_path, encoding='utf8') as f:
            return toml.load(f)

    def test_title(self):
        """titleが「喫煙室利用者数カウント」であること"""
        title = self.driver.find_element_by_tag_name('title')

        expected = '喫煙室利用者数カウント'
        actual = title.get_attribute('innerHTML')
        assert expected == actual

    def test_is_displayed_count_of_last_line_of_csv(self):
        """カードに表示されている検知人数がCSVの最終行と一致すること"""
        csv_file = 'E:\\project\\smoking-area-count\\' \
                   'backend\\src\\test_file\\video_source.csv'
        rows = self.open_csv(csv_file)
        last_row = rows[-1]
        expected = last_row[-1] + '人'

        tag = 'room_use_wrap'
        elements = self.driver.find_elements_by_class_name(tag)
        element = elements[0]
        detects = element.find_elements_by_tag_name('div')
        detect = detects[1].get_attribute('innerHTML')

        assert expected == detect

    def test_csv_change(self):
        # implemented yet
        pass

    def teardown_method(self):
        # ブラウザを終了する
        self.driver.close()
