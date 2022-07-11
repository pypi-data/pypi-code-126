import psutil
import os
import time
from livereload import Server, shell
server = Server()
server.watch('CheckUtil.py', delay=5)
server.serve(root='build\lib\CheckUtil')

class CheckUtil:
    
    def cpu_usage():
        process = psutil.Process(os.getpid())
        for i in range(10):
            print(process.cpu_percent())
            time.sleep(300)
        

    def ram_usage():
        process = psutil.Process(os.getpid())
        for i in range(10):
            print(process.memory_percent())
            time.sleep(300)

    def disk_usage():
        process = psutil.Process(os.getpid())
        for i in range(10):
            print(process.disk_usage())
            time.sleep(300)
