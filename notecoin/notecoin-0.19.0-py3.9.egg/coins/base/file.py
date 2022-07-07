from datetime import datetime


class DataFileSystem:
    def __init__(self, exchange_name='okex', data_type='kline',
                 path='~/workspace/tmp/notecoin', freq='daily', timeframe='1m', file_format='%Y%m%d'):
        self.path = path
        self.freq = freq
        self.data_type = data_type
        self.timeframe = timeframe
        self.file_format = file_format
        self.exchange_name = exchange_name

    @property
    def file_path_dir(self):
        return f"{self.path}/{self.exchange_name}/{self.data_type}-{self.freq}-{self.timeframe}"

    def filename_prefix(self, start_date):
        return f"{self.exchange_name}-{self.data_type}-{self.freq}-{self.timeframe}-{start_date.strftime(self.file_format)}"

    def file_path_csv(self, start_date):
        return f"{self.file_path_dir}/{self.filename_prefix(start_date)}.csv"

    def file_path_tar(self, start_date):
        return f"{self.file_path_dir}/{self.filename_prefix(start_date)}.tar.gz"

    def file_path_tar_gz(self, start_date):
        return f"{self.file_path_dir}/{self.filename_prefix(start_date)}.tar.gz"

    def file_path_tar_xz(self, start_date):
        return f"{self.file_path_dir}/{self.filename_prefix(start_date)}.tar.xz"
