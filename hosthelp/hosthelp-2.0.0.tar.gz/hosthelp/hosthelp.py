import os
import time
def reqedit(requirements_filename='requirements'):
    start_time = time.time()
    file_ = open(f'{requirements_filename}.txt', 'r+')
    requires = file_.read()
    requires = requires.split()
    requires = [i + '==' + j for i, j in zip(requires[::2], requires[1::2])]

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{requirements_filename}.txt')
    os.remove(path)
    file_ = open("requirements.txt", "w+")
    file_.write('\n'.join(requires))
    return f'Задача была выполнена успешно за {(time.time() - start_time)} секунд'
def createproc(py):
    start_time = time.time()
    procfile=open('Procfile','w+')
    procfile.write(f'web: python {py}.py')
    return f'Задача была выполнена успешно за {(time.time() - start_time)} секунд'