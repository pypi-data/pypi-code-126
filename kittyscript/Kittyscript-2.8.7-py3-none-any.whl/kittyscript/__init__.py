import random
import hashlib
import time

def say(Print):
    print(Print)

def addnum(x, y):
    print(x + y)

def addfloat(f1, f2):
    print(f1+ f2)

def Divide(a, b):
    print(a / b)

def genaratenumber(Low_number, High_number):
    x = random.randint(Low_number, High_number)

    print(x)

Pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062
E = 2.71828


def version():
    print("v2.8.7 Red-Army")

def CreateFile(name, content):
    with open(name, 'w') as foo:
        foo.write(content)

def Appendtofile(name, content):
    with open(name, 'a') as foo0:
        foo0.append(content)

def kill():
    exit()

def hashshaw256(Hashtext):
    my_str = Hashtext
    my_hash = hashlib.sha256(my_str.encode('utf-8')).hexdigest()
    print(my_hash)

def curtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

def help():
    print("https://github.com/Iwertyuiop123653/kitty-script-/wiki")