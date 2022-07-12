import logging
import os
from datetime import datetime

from notecoin.base.database.lanzou import LanzouDirectory
from notecoin.coins.base.load import LoadDataKline
from notecoin.utils.time import day_during, month_during, week_during
from notefile.compress import tarfile

logger = logging.getLogger()


class DataFileProperty:
    def __init__(self, exchange, data_type='kline', path='~/workspace/tmp', start_date=datetime.today(),
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
        self.drive = LanzouDirectory(fid=5679873)

    def file_path_dir(self, absolute=True):
        path = f"notecoin/{self.exchange_name}/{self.data_type}-{self.freq}-{self.timeframe}"
        if absolute:
            path = f"{self.path}/{path}"
            if not os.path.exists(path):
                os.makedirs(path)
        return path

    @property
    def filename_prefix(self):
        return f"{self.exchange_name}-{self.data_type}-{self.freq}-{self.timeframe}-{self.start_date.strftime(self.file_format)}"

    def file_path_csv(self, absolute=True):
        return f"{self.file_path_dir(absolute)}/{self.filename_prefix}.csv"

    def file_path_tar(self, absolute=True):
        return f"{self.file_path_dir(absolute)}/{self.filename_prefix}.tar"

    def arcname(self, file):
        return os.path.join(self.file_path_dir(False), os.path.basename(file))

    def sync(self):
        self.drive.scan_all_file()
        self.drive.sync(f'{self.path}/notecoin')

    def tar_exists(self):
        if self.drive.file_exist(self.file_path_tar(False)):
            return True
        if os.path.exists(self.file_path_tar()):
            return False

    def _load_and_save(self) -> bool:
        self.sync()
        if self.tar_exists():
            return False
        logger.info(f'download for {self.file_path_tar(absolute=False)}')
        exchan = LoadDataKline(self.exchange)
        exchan.table.delete_all()
        unix_start, unix_end = int(self.start_date.timestamp() * 1000), int(self.end_date.timestamp() * 1000)
        # 下载
        exchan.load_all(timeframe=self.timeframe, unix_start=unix_start, unix_end=unix_end)
        # 保存
        exchan.table.to_csv_all(self.file_path_csv(), page_size=100000)
        # 压缩
        with tarfile.open(self.file_path_tar(), "w:xz") as tar:
            tar.add(self.file_path_csv(), arcname=self.arcname(self.file_path_csv()))
        # 删除
        os.remove(self.file_path_csv())
        exchan.table.delete_all()
        return True

    def _load(self, start_end_fun):
        index = 1
        while index < 10:
            self.start_date, self.end_date = start_end_fun(-index)
            if self._load_and_save():
                index += 1

    def load(self):
        if self.freq == 'daily':
            self.file_format = '%Y%m%d'
            self._load(day_during)
        elif self.freq == 'weekly':
            self.file_format = '%Y%m%d'
            self._load(week_during)
        elif self.freq == 'monthly':
            self.file_format = '%Y%m'
            self._load(month_during)
