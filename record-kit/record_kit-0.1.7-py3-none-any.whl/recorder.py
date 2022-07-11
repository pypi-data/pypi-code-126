import pathlib
import time
import os
import warnings


def check_suffix(file_name):
    suffixes = file_name.suffixes
    if len(suffixes) < 1 or suffixes[-1] != '.md':
        suffixes.append('.md')
        suffix = ''.join(suffixes)
        file_name.with_suffix(suffix)
    return str(file_name.absolute())


class LogBase:
    def __init__(self, file_path):
        self.file_path = file_path

    def append(self, s):
        with self.file_path.open("a") as f:
            f.write(s)

    def append_line(self, s):
        with self.file_path.open("a") as f:
            f.write(s + "\n")


class Recorder(LogBase):
    def __init__(self, file_name='record', records_dir='./records', with_timestamp=True):
        self.records_dir = pathlib.Path(records_dir)
        try:
            os.mkdir(self.records_dir)
        except FileExistsError:
            pass
        if with_timestamp:
            timestamp = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
            file_name += '-' + timestamp
        self.record_name = self.records_dir.joinpath(file_name + '.md')
        self.meta_added = False
        self.header_added = False
        self._data_fields_num = 0
        super().__init__(self.record_name)
        self.append_line(f"# {file_name}")

    def _begin_meta(self):
        s = "## Meta\n" + \
            "| key | value | type |\n" + \
            "| :---: |  :---: | :---: |\n"
        self.append(s)

    def _begin_data(self):
        s = "## Data"
        self.append_line(s)

    def set_meta(self, meta_info):
        if self.meta_added:
            warnings.warn('Meta information can only be added once')
            return

        self.meta_added = True
        self._begin_meta()
        if isinstance(meta_info, dict):
            pass
        else:
            meta_info = meta_info.__dict__
        for key, value in meta_info.items():
            s = f"| {key} | {str(value)} | {type(value).__name__} |"
            self.append_line(s)

    def set_header(self, *args):
        if self.header_added:
            warnings.warn('Table header can only be added once')
            return
        self.header_added = True

        self._begin_data()
        length = len(args)
        self._data_fields_num = length
        args = map(str, args)
        s = " | ".join(args)
        s = "| " + s + " |"
        s2 = "| :---: " * length + "|"
        self.append_line(s)
        self.append_line(s2)

    def add_data(self, *args):
        if len(args) != self._data_fields_num:
            raise ValueError(
                f'mismatch between the number of fields({self._data_fields_num}) and the number of data({len(args)})'
            )
        args = map(str, args)
        s = " | ".join(args)
        s = "| " + s + " |"
        self.append_line(s)