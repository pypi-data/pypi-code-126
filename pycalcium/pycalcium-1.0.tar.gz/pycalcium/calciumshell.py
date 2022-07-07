from sys import argv, exit
from calcium import Calcium
version = '1.1'

def shell():
    print("Welcome to Calcium Shell v" + version)
    print("")
    while True:
        inp = input("> ").lower()
        if inp == "exit":
            exit(0)
        elif inp == "bye":
            exit(0)
        elif inp == "quit":
            exit(0)
        else:
            eq = Calcium(inp)
            print(eq.solve())
if len(argv) < 2:
    shell()
else:
    eq = Calcium(" ".join(argv[1:]))
    print(eq.solve())