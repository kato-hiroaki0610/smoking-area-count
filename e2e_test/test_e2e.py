import csv
import time

import pytest  # noqa
from selenium import webdriver


class TestSmokingAreaCount(object):
    def setup_method(self):
        # Selenium Server に接続する
        self.driver = webdriver.Chrome()
        # Selenium 経由でブラウザを操作する
        self.driver.get('http://localhost:8000/web/index.html')
        time.sleep(5)
        print(self.driver.current_url)

    def test_title(self):
        """titleが「喫煙室利用者数カウント」であること"""
        title = self.driver.find_element_by_tag_name('title')

        expected = '喫煙室利用者数カウント'
        actual = title.get_attribute('innerHTML')
        assert expected == actual

    def test_is_displayed_count_of_last_line_of_csv(self):
        csv_file = 'E:\\project\\smoking-area-count\\' \
                   'backend\\src\\test_file\\video_source.csv'
        with open(csv_file, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            # iteratorをリストに変換する
            rows = [r for r in reader]
        last_row = rows[-1]
        detected = last_row[-1]

        # elements = self.driver.find_elements_by_class('card')
        elements = self.driver.find_element_by_css_selector('card > div:nth-child(2)')

        expected = detected
        element = elements[0]

        assert expected == element.get_attribute('innerHTML')

    def test_csv_change(self):
        # implemented yet
        pass

    def teardown_method(self):
        # ブラウザを終了する
        self.driver.close()
