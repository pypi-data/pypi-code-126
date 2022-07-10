import os

from pypcreate.utils import load_yaml
from pypcreate.utils import create_files
from pypcreate.utils import create_a_file
from pypcreate.utils import download_github_file
from pypcreate.utils import create_empty

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

def mk_subdir(directory,parent_path):
    dir_key = list(directory.keys())
    for item in dir_key:
        if item == 'dir_name':  
            dir_name = directory['dir_name']
            mkdir(dir_name)
        elif item == 'files':
            create_files(dir_name,directory['files'])
        else:
            if parent_path == 'root':
                mk_subdir(directory[item],'None')   
            else:
                directory[item]['dir_name'] = os.path.join(dir_name,directory[item]['dir_name'])
                mk_subdir(directory[item],dir_name) 

def setpyp():
    create_empty('setup.py')
    create_empty('environment.yml')
    create_empty('MANIFEST.in')
    
def pyptemp():
    MANIFEST_url = 'https://raw.githubusercontent.com/zhz03/PyPCreate/main/pysetup_template/MANIFEST.in'
    download_github_file(MANIFEST_url)
    env_url = 'https://raw.githubusercontent.com/zhz03/PyPCreate/main/pysetup_template/environment.yml'
    download_github_file(env_url)
    setup_url = 'https://raw.githubusercontent.com/zhz03/PyPCreate/main/pysetup_template/setup.py'
    download_github_file(setup_url)

def inittemp():
    init_url = 'https://raw.githubusercontent.com/zhz03/PyPCreate/main/pysetup_template/__init__.py'
    download_github_file(init_url)

if __name__ == '__main__':
    inittemp()

    

        
        
        
    
