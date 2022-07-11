# @Time    : 2022/6/23 15:44
# @Author  : chengwenxian@starmerx.com
# @Site    : 
# @Software: PyCharm
# @Project : amazon_project
# TODO:  使用自定义Logger启动客户端
# 通过自定义得Logger, 可以指定日志输入流向

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from ..apollo_client import ApolloClient


APOLLO_CONFIG_URL = 'your config server url'
APOLLO_APP_ID = 'your application id'
APOLLO_ACCESS_KEY_SECRET = 'the secret for your application'


def gen_logger():
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    log_dir_path = os.path.join(base_dir, 'logs/apollo')
    log_path = os.path.join(log_dir_path, '{date}.log'.format(date=datetime.now().strftime('%Y-%m-%d')))
    os.makedirs(log_dir_path, exist_ok=True)

    logger = logging.getLogger(__name__)
    fh = TimedRotatingFileHandler(filename=log_path, when='d', backupCount=3, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'))
    logger.addHandler(fh)
    return logger


logger = gen_logger()
a_client = ApolloClient(
    app_id=APOLLO_APP_ID, secret=APOLLO_ACCESS_KEY_SECRET, config_url=APOLLO_CONFIG_URL, logger=logger
)

