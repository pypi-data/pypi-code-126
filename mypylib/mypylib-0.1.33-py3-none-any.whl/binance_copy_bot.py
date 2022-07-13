#
# Memo
# For MAC: xattr -d com.apple.quarantine chromedriver
#

import threading
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger
import os
import orjson
import json

from mypylib import tLineNotify



class Binance_position_monitor(threading.Thread):
    url_format = 'https://www.binance.com/en/futures-activity/leaderboard/user?uid={}&tradeType=PERPETUAL'

    def __init__(self,
                 chrome_location='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                 driver_location='/usr/local/bin/chromedriver',
                 file_monitor_list='./binance_watch_list.txt',
                 dir_positions_logger='.'):
        threading.Thread.__init__(self)
        self.to_stop = threading.Event()

        self.chrome_location = chrome_location
        self.driver_location = driver_location
        self.file_monitor_list = file_monitor_list
        self.dir_positions_logger = dir_positions_logger

        self.driver = None

        self.init_driver()


        self.sleep_period = 6

        self.list_victim = []

        self.count_usage = 0
        self.count_max_usages = 60

        self.line_sender: tLineNotify = None

    def init_driver(self):
        if self.driver is not None:
            self.driver.quit()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        options.binary_location = self.chrome_location
        options.add_argument("--headless")
        options.add_argument("--disable-web-security")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(self.driver_location, options=options)

        self.count_usage = 0

    @logger.catch
    def load_victim_list(self):
        with open(self.file_monitor_list) as fp:
            for line in fp.readlines():
                if len(line) == 0:
                    continue
                if line[0] == '#':
                    continue
                fields = line.split(' ')
                if len(fields) != 2:
                    continue
                self.list_victim.append([fields[0], fields[1].rstrip()])

    def run(self):
        while not self.to_stop.is_set():
            self.count_usage += 1
            if self.count_usage > self.count_max_usages:
                self.init_driver()

            self.load_victim_list()

            for name, uid in self.list_victim:
                logger.info(f'{name} {uid}')

                try:
                    url = self.url_format.format(uid)
                    self.driver.get(url)
                    print(url)
                except Exception as e:
                    logger.error(f"{e}\ncannot fetch url")
                    continue

                try:
                    # TODO: 這邊有問題，還需要修改
                    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "thead")))
                except Exception as e:
                    logger.error(f"{e}\ncannot get webpage.")
                    continue

                sleep(self.sleep_period)

                try:
                    page_source = self.driver.page_source
                    soup = BeautifulSoup(page_source, features="html.parser")
                    pretty_soup = soup.prettify()
                    # print(pretty_soup)
                    tables = pd.read_html(pretty_soup)
                    logger.info(f'{datetime.now()} {name}')
                    if len(tables) < 5:
                        print(f'table len: {len(tables)}')
                    else:
                        print(tables[4])
                        table_position = tables[4]
                        table_position.set_index('Symbol', inplace=True)
                        dict_now_positions = table_position.to_dict('index')

                        path_position_logger = f'{self.dir_positions_logger}/{uid}.json'
                        if not os.path.isfile(path_position_logger):
                            with open(path_position_logger, 'w+') as fp:
                                json.dump(dict_now_positions, fp)
                            continue

                        with open(path_position_logger) as fp:
                            dict_org_positions = json.load(fp)

                        for symbol in dict_now_positions.keys():
                            if symbol not in dict_org_positions.keys():
                                msg = f'建立新部位: {symbol}, Size: {dict_now_positions[symbol]["Size"]}, Enter price: {dict_now_positions[symbol]["Entry Price"]}, Mark price: {dict_now_positions[symbol]["Entry Price"]}'
                                if self.line_sender is not None:
                                    self.line_sender.send(msg)
                                logger.info(msg)

                        for symbol in dict_org_positions.keys():
                            if symbol not in dict_now_positions.keys():
                                msg = f'平倉舊部位: {symbol}, Size: {dict_org_positions[symbol]["Size"]}, Enter price: {dict_org_positions[symbol]["Entry Price"]}, Mark price: {dict_org_positions[symbol]["Entry Price"]}'
                                if self.line_sender is not None:
                                    self.line_sender.send(msg)
                                logger.info(msg)

                        for symbol in dict_now_positions.keys():
                            if symbol not in dict_org_positions.keys():
                                continue
                            if dict_now_positions[symbol]['Size'] != dict_org_positions[symbol]['Size']:
                                msg = f'部位改變: {symbol}, Size: [{dict_org_positions[symbol]["Size"]}] -> [{dict_now_positions[symbol]["Size"]}]'
                                if self.line_sender is not None:
                                    self.line_sender.send(msg)
                                logger.info(msg)

                        with open(path_position_logger, 'w+') as fp:
                            json.dump(dict_now_positions, fp)
                except Exception as e:
                    logger.error(e)

    def stop(self):
        self.to_stop.set()


if __name__ == '__main__':
    bpm = Binance_position_monitor()
    bpm.line_sender = tLineNotify('9RV6KI0eN0sqI8SlvvGiMTrd7tPYu9qB4m3L2rnQNVl')

    bpm.run()
