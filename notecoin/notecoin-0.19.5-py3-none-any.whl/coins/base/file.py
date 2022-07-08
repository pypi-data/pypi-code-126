import os
from datetime import datetime

from notedrive.lanzou import LanZouDrive


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
        self.drive = LanZouDrive()
        self.drive.ignore_limits()
        self.drive.login_by_cookie()

    @property
    def file_path_dir(self):
        path = f"{self.path}/notecoin/{self.exchange_name}/{self.data_type}-{self.freq}-{self.timeframe}"
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

    def arcname(self, file):
        path = self.file_path_dir.replace(f"{self.path}/", "")
        return os.path.join(path, os.path.basename(file))

    def sync(self):
        self.drive.sync_files(self.path, '5679873', only_directory=False)
