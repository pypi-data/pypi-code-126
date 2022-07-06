from colorama import Fore,Style,init
import os

if not os.environ.get("forceColor") == "1":
    init()

class Test:

    def __init__(self):
        self.tests = []
    
    def test(self,condition,testName,**kwargs):
        self.tests.append({
            "result":"pass" if condition else "fail",
            "name": testName,
            "kwargs": kwargs
        })
    
    def print(self):
        print("---------------")
        for test in self.tests:
            print("\033[1m" + "Name: " + Style.RESET_ALL + Fore.CYAN + test["name"] + Style.RESET_ALL)
            print("\033[1m" + "Result: " + Style.RESET_ALL + (Fore.GREEN if test["result"] == "pass" else Fore.RED) + test["result"] + Style.RESET_ALL)
            for key in test["kwargs"]:
                print(Style.DIM + str(key) + " = " + str(test["kwargs"][key]))
            print(Style.RESET_ALL+"---------------")
        if any([item["result"] == "fail" for item in self.tests]):
            os.environ["testsFailed"] = "1"