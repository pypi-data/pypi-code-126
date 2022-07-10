import os
from pypcreate.utils import load_yaml
from pypcreate.utils import mk_subdir

def mkdir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        init_path = os.path.join(dir_name,"__init__.py")
        readme_path = os.path.join(dir_name,"README.md")
        if not os.path.exists(readme_path):
            open(readme_path, "x")
        else:
            print(" '__init__.py' already exists in your directory. ")
        if not os.path.exists(init_path):
            open(init_path, "x")
        else:
            print(" 'README.md' already exists in your directory. ")
    else:
        print("This path already exists!")

def mkdir_from_yaml(yaml_file_name):
    param = load_yaml(yaml_file_name)
    mk_subdir(param['root'],'root')

if __name__ == '__main__':
    mkdir("hello")
    param = mkdir_from_yaml('example.yaml')
    mk_subdir(param['root'],'root')
    

        
        
        
    