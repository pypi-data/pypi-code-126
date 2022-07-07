with open('desideratatxt.txt', 'r') as f:
    contents = f.read()

def desiderata() -> str:
    return contents