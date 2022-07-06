import random
from .custom_utils.today_date import print_today_date

def ok():
    print("okay")

def say_hello_again():
    print_today_date()
    print("hello again!!!")
    print(random.choice(["Yes", "No"]))
    ok()