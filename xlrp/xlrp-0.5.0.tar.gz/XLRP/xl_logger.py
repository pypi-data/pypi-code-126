import datetime
import threading


_lock = threading.RLock()
def _set_color(color, msg):
    return f'\033[1;50;{color}m{msg}\033[0m'

def _now_time():
    return str(datetime.datetime.now())

def _logger_write(filename=None, msg=None):
    _lock.acquire()
    if filename is None:
        return
    else:
        with open(filename, 'a', encoding='utf8') as f:
            f.writelines(msg)
            f.close()
    _lock.release()

class Logger:
    def __init__(self, path=None):
        self.path = path

    def success(self, msg):
        print(_set_color(32, _now_time() + ' ' + msg))
        _logger_write(self.path, _now_time() + ' ' + msg + '\n')

    def error(self, msg):
        print(_set_color(32, _now_time() + ' ' + msg))
        _logger_write(self.path, _now_time() + ' ' + msg + '\n')

