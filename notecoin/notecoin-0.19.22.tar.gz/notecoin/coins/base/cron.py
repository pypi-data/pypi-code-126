import logging
import os

from ccxt import okex
from notecoin.coins.base.file import DataFileProperty
from notecoin.coins.base.load import LoadDataKline
from notecoin.utils.time import day_during, month_during, week_during
from notefile.compress import tarfile

logger = logging.getLogger()


def load_and_save(file_pro: DataFileProperty):
    file_pro.sync()

    if file_pro.tar_exists():
        return

    exchan = LoadDataKline(file_pro.exchange)
    exchan.table.delete_all()
    unix_start, unix_end = int(file_pro.start_date.timestamp() * 1000), int(file_pro.end_date.timestamp() * 1000)
    # 下载
    exchan.load_all(timeframe=file_pro.timeframe, unix_start=unix_start, unix_end=unix_end)
    # 保存
    exchan.table.to_csv_all(file_pro.file_path_csv(), page_size=100000)
    # 压缩
    with tarfile.open(file_pro.file_path_tar(), "w:xz") as tar:
        tar.add(file_pro.file_path_csv(), arcname=file_pro.arcname(file_pro.file_path_csv()))
    # 删除
    os.remove(file_pro.file_path_csv())
    exchan.table.delete_all()


def load_monthly(file_pro: DataFileProperty):
    file_pro.freq = 'monthly'
    file_pro.file_format = '%Y%m'
    for index in range(1, 12*3):
        file_pro.start_date, file_pro.end_date = month_during(-index)
        load_and_save(file_pro)


def load_weekly(file_pro: DataFileProperty):
    file_pro.freq = 'weekly'
    file_pro.file_format = '%Y%m%d'
    for index in range(1, 54*3):
        file_pro.start_date, file_pro.end_date = week_during(-index)
        load_and_save(file_pro)


def load_daily(file_pro: DataFileProperty):
    file_pro.freq = 'daily'
    file_pro.file_format = '%Y%m%d'
    for index in range(1, 365*3):
        file_pro.start_date, file_pro.end_date = day_during(-index)
        load_and_save(file_pro)


path_root = '/home/bingtao/workspace/tmp'

file_pro = DataFileProperty(exchange=okex(), freq='daily', path=path_root, timeframe='1m')
# load_daily(file_pro)
# load_weekly(file_pro)
# file_pro.sync()
file_pro.load()
