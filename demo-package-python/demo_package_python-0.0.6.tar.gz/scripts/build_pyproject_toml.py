import toml

def get_requirements_list(): 
    requirements = []
    data = open("./requirements.txt", "r").read()
    lines = data.split("\n")
    lines = [] 
    for i in range(len(lines)):
        line = lines[i]
        tokens = line.split("==")
        newline = tokens[0] + " == " + tokens[1]
    return lines

data = toml.load("pyproject.dev.toml")
data['project']['dependencies'] = get_requirements_list() 
contents = toml.dumps(data) 

open("pyproject.toml", "w").write(contents)