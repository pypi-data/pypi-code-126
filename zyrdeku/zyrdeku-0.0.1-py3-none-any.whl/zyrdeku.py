from time import*
from alive_progress import alive_bar
import os
import time
import sys
def cc(text):
    timee = 0.1
    for i in text:
        sleep(timee)
        print(i,end='',flush = True)
        sys.stdout.flush()
    print("",end="\n")
    return ""

def getsum():
    a = 0
    b = 0
    sue = 0
    a = int(input(cc("请输入数的个数:")))
    cc("ok!,稍等·············")
    print("已完成")
    for i in range(a):
        b = int(input(cc("请输入数字:")))
        sue = sue + b
    cc("正在计算中···········")
    cc("计算完毕")
    cc("结果为:")
    print(sue)

def jindu():
    with alive_bar(100,force_tty=True) as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()