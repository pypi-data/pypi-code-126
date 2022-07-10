import datetime, sys, os

class logger:
    def debug(self, input):
        self.frame = sys._getframe(1)
        print('\x1b[32m%s \033[0m| \033[1m\x1b[34mDEBUG    \033[0m| \x1b[96m%s\033[0m:\x1b[96m%s\033[0m:\x1b[96m%s \033[0m- \033[1m\x1b[34m%s\033[0m' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], os.path.basename(self.frame.f_code.co_filename), self.frame.f_code.co_name, self.frame.f_lineno, input))

    def success(self, input):
        self.frame = sys._getframe(1)
        print('\x1b[32m%s \033[0m| \033[1m\x1b[32mSUCCESS  \033[0m| \x1b[96m%s\033[0m:\x1b[96m%s\033[0m:\x1b[96m%s \033[0m- \033[1m\x1b[32m%s\033[0m' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], os.path.basename(self.frame.f_code.co_filename), self.frame.f_code.co_name, self.frame.f_lineno, input))

    def error(self, input):
        self.frame = sys._getframe(1)
        print('\x1b[32m%s \033[0m| \033[1m\x1b[31mERROR    \033[0m| \x1b[96m%s\033[0m:\x1b[96m%s\033[0m:\x1b[96m%s \033[0m- \033[1m\x1b[31m%s\033[0m' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], os.path.basename(self.frame.f_code.co_filename), self.frame.f_code.co_name, self.frame.f_lineno, input))

    def warning(self, input):
        self.frame = sys._getframe(1)
        print('\x1b[32m%s \033[0m| \033[1m\x1b[33mWARNING  \033[0m| \x1b[96m%s\033[0m:\x1b[96m%s\033[0m:\x1b[96m%s \033[0m- \033[1m\x1b[33m%s\033[0m' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], os.path.basename(self.frame.f_code.co_filename), self.frame.f_code.co_name, self.frame.f_lineno, input))

    def info(self, input):
        self.frame = sys._getframe(1)
        print('\x1b[32m%s \033[0m| \033[1mINFO     \033[0m| \x1b[96m%s\033[0m:\x1b[96m%s\033[0m:\x1b[96m%s \033[0m- \033[1m%s\033[0m' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], os.path.basename(self.frame.f_code.co_filename), self.frame.f_code.co_name, self.frame.f_lineno, input))

logger = logger()