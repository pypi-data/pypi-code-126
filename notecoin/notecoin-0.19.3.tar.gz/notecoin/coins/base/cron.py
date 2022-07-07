import logging
import os
from datetime import datetime

from ccxt import okex
from notecoin.coins.base.load import LoadDataKline
from notecoin.utils.time import day_during, month_during, week_during
from notedrive.lanzou import LanZouDrive
from notefile.compress import tarfile

logger = logging.getLogger()


class DataFileProperty:
    def __init__(self, exchange, data_type='kline', path='~/workspace/tmp/notecoin', start_date=datetime.today(),
                 end_date=datetime.today(), freq='daily', timeframe='1m', file_format='%Y%m%d'):
        self.path = path
        self.freq = freq
        self.exchange = exchange
        self.data_type = data_type
        self.timeframe = timeframe
        self.start_date = start_date
        self.end_date = end_date
        self.file_format = file_format
        self.exchange_name = exchange.name.lower()
        self.drive = LanZouDrive()

    @property
    def file_path_dir(self):
        path = f"{self.path}/{self.exchange_name}/{self.data_type}-{self.freq}-{self.timeframe}"
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @property
    def filename_prefix(self):
        return f"{self.exchange_name}-{self.data_type}-{self.freq}-{self.timeframe}-{self.start_date.strftime(self.file_format)}"

    @property
    def file_path_csv(self):
        return f"{self.file_path_dir}/{self.filename_prefix}.csv"

    @property
    def file_path_tar(self):
        return f"{self.file_path_dir}/{self.filename_prefix}.tar.gz"

    @property
    def file_path_tar_gz(self):
        return f"{self.file_path_dir}/{self.filename_prefix}.tar.gz"

    @property
    def file_path_tar_xz(self):
        return f"{self.file_path_dir}/{self.filename_prefix}.tar.xz"

    def sync(self):
        self.drive.sync_directory(self.path, '5679873')


def load_and_save(file_pro: DataFileProperty):
    exchan = LoadDataKline(file_pro.exchange)
    unix_start, unix_end = int(file_pro.start_date.timestamp() * 1000), int(file_pro.end_date.timestamp() * 1000)

    if os.path.exists(file_pro.file_path_tar_xz):
        logger.info("file exists.")
        return
    # 下载
    exchan.load_all(timeframe=file_pro.timeframe, unix_start=unix_start, unix_end=unix_end)
    # 保存
    exchan.table.to_csv_all(file_pro.file_path_csv, page_size=100000)
    # 压缩
    with tarfile.open(file_pro.file_path_tar_xz, "w:xz") as tar:
        tar.add(file_pro.file_path_csv)
    # 删除
    os.remove(file_pro.file_path_csv)
    exchan.table.delete_all()


def load_monthly(file_pro: DataFileProperty):
    file_pro.freq = 'monthly'
    file_pro.file_format = '%Y%m'
    for index in range(1, 10):
        file_pro.start_date, file_pro.end_date = month_during(-index)
        load_and_save(file_pro)


def load_weekly(file_pro: DataFileProperty):
    file_pro.freq = 'weekly'
    file_pro.file_format = '%Y%m%d'
    for index in range(1, 10):
        file_pro.start_date, file_pro.end_date = week_during(-index)
        load_and_save(file_pro)


def load_daily(file_pro: DataFileProperty):
    file_pro.freq = 'daily'
    file_pro.file_format = '%Y%m%d'
    for index in range(1, 10):
        file_pro.start_date, file_pro.end_date = day_during(-index)
        load_and_save(file_pro)


path_root = '/home/bingtao/workspace/tmp/notecoin'

file_pro = DataFileProperty(exchange=okex(), path=path_root, timeframe='1m')
load_daily(file_pro)
