import csv
import pathlib
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
        print(self.driver.current_url)

    def open_csv(self, file_path):
        """CSVを開く"""
        with open(file_path, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            # iteratorをリストに変換する
            rows = [r for r in reader]

        return rows

    def create_csv(self, csv_data, file_name):
        """CSVを作成する"""
        pathlib.Path('./\\' + file_name).touch()

        with open(file_name, 'w', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

    def remove_csv(self, file_name):
        """CSVを削除する"""
        pathlib.Path(file_name).unlink()

    def rewrite_csv_path(self, csv_file_name, index, is_use_or_wait):
        """setting用のtomlファイルを編集する"""
        setting_dir = 'bin\\setting'
        setting_file = 'setting.toml'

        toml_data = toml.load(open(f'{setting_dir}\\{setting_file}',
                              encoding='utf8'))
        csv_path = str(pathlib.Path.cwd() / csv_file_name)
        toml_data['area'][index][is_use_or_wait] = csv_path
        with open(f'{setting_dir}\\{setting_file}', 'w',
                  encoding='utf8') as fp:
            toml.dump(toml_data, fp)

    def test_title(self):
        """titleが「喫煙室利用者数カウント」であること"""
        title = self.driver.find_element_by_tag_name('title')

        expected = '喫煙室利用者数カウント'
        actual = title.get_attribute('innerHTML')
        assert expected == actual

    def test_is_displayed_info(self):
        """設定ファイルに記載されている情報がすべて表示されていること"""
        setting_dir = 'bin\\setting'
        setting_file = 'setting.toml'

        toml_data = toml.load(open(f'{setting_dir}\\{setting_file}',
                              encoding='utf8'))
        expected_info = toml_data['area'][0]

        elements = self.driver.find_elements_by_class_name('card')

        for i, expected in enumerate(expected_info.keys()):
            actual = elements[0].get_attribute('innerHTML')
            if expected == '場所':
                assert expected_info[expected] in actual
            elif expected == '待ち人数':
                assert '待機中' in actual
            else:
                assert expected in actual

    def test_is_displayed_count_of_last_line_of_csv(self):
        """カードに表示されている検知人数がCSVの最終行と一致すること"""
        csv_data = {
                    'tmp.csv': [['a', 'b', 'c', 'd', '5'],
                                ['a', 'b', 'c', 'd', '6'],
                                ['a', 'b', 'c', 'd', '5']],
                    'tmp2.csv': [['a', 'b', 'c', 'd', '20']],
                    'tmp3.csv': [['a', 'b', 'c', 'd', '100']],
                    'tmp4.csv': [['a', 'b', 'c', 'd', '1']],
        }
        csv_files = ['tmp.csv', 'tmp2.csv', 'tmp3.csv', 'tmp4.csv']
        for f in csv_files:
            self.create_csv(csv_data[f], f)

        use = '利用者'
        wait = '待ち人数'
        rewrite_data = [
                {'path': csv_files[0], 'index': 0, 'use_or_wait': use},
                {'path': csv_files[0], 'index': 0, 'use_or_wait': wait},
                {'path': csv_files[1], 'index': 1, 'use_or_wait': use},
                {'path': csv_files[1], 'index': 1, 'use_or_wait': wait},
                {'path': csv_files[2], 'index': 2, 'use_or_wait': use},
            ]
        for i in rewrite_data:
            self.rewrite_csv_path(i['path'], i['index'], i['use_or_wait'])
        time.sleep(5)

        tags = ['room_use_wrap', 'room_wait_wrap']
        for i in range(len(tags)):
            elements = self.driver.find_elements_by_class_name(tags[i])

            expecteds = [['5人', '20人', '100人'], ['5人', '20人', '0人']]
            for j in range(len(expecteds[0])):
                element = elements[j]
                detects = element.find_elements_by_tag_name('div')
                detect = detects[1].get_attribute('innerHTML')

                assert expecteds[i][j] == detect

        for f in csv_files:
            self.remove_csv(f)

    def test_csv_change(self):
        """CSVが更新されたらリアルタイムに反映されること"""
        pass

    def teardown_method(self):
        # ブラウザを終了する
        self.driver.close()
