import logging
import sys
import os


class Logger:
    def __init__(self, log_path: str, log_name: str, log_level=20) -> None:
        self.log_path = log_path
        self.log_name = log_name
        self.my_log_level = logging.INFO

        if not os.path.isdir(f'{self.log_path}/log'):
            os.mkdir(f'{self.log_path}/log')

        if not os.path.isfile(f'{self.log_path}/id.txt'):
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write('1')
                self.id = 1
        else:
            with open(f'{self.log_path}/id.txt', 'r') as ids:
                self.id = int(ids.read())

        if self.id > 10:
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write(str(1))
        else:
            with open(f'{self.log_path}/id.txt', 'w') as ids:
                ids.write(str(self.id+1))

        self.set_log_level(log_level)
        self.infoLogger()

    def set_log_level(self, log: int) -> None:
        if not isinstance(log, int):
            raise ValueError(f'Required an int not {type(log)}')

        if log not in [10, 20, 30, 40, 50]:
            raise ValueError('Unsupported log type.')

        self.my_log_level = log

    def infoLogger(self) -> None:

        _log = logging.getLogger(self.log_name)
        _log.setLevel(self.my_log_level)

        _format = '%(asctime)s [%(filename)s : %(funcName)s()] ' + \
            '%(levelname)s: %(message)s'
        _datefmt = '%m/%d/%Y %I:%M:%S %p'
        _filepath = f'{self.log_path}/log/log_{self.id}.log'

        formatter = logging.Formatter(_format, datefmt=_datefmt)

        fileHandler = logging.FileHandler(_filepath, mode='w')
        fileHandler.setFormatter(formatter)
        _log.addHandler(fileHandler)

        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(formatter)
        _log.addHandler(streamHandler)


if __name__ == '__main__':
    print(type(logging.INFO))
