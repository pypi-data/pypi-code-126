import random
import hashlib
import time
import string
import os

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

Things_That_can_kill = ["🌱 Household Plants", "Lint", "♋ Cancer", "🥔 Overripe Potatoes", "Black licorice"]

def version():
    print("v2.9.2 farted-tart")

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

def wait(time_to_wait):
    time.sleep(time_to_wait)

def spyware(key_):
    import keyboard
    recorded_events = keyboard.record(key_)
    CreateFile("keylogged.txt", recorded_events)

def coinflip():
    head_or_tales = ["Tales", "Heads"]
    who_wins = random.choices(head_or_tales)
    print(who_wins)

def dice_roll():
    dice_sides = [1, 2, 3, 4, 5, 6]
    dice_side = random.choices(dice_sides)
    print(dice_side)

def checkemail(email):
    import re
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")

def randomstring():
    print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)))

def run(name_of_python_file):
    os.system(name_of_python_file)