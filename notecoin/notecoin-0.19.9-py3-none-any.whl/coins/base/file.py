import os
from datetime import datetime

from notecoin.base.database.lanzou import LanzouDirectory


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
        self.drive.sync(f'{self.path}/notecoin')

    def tar_exists(self):
        if self.drive.file_exist(self.file_path_tar(False)):
            return True
        if os.path.exists(self.file_path_tar()):
            return False
