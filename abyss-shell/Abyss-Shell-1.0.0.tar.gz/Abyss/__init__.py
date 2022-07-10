from colorama import Fore, Back, init
from os import error, system, truncate
from tqdm import tqdm
import pyfiglet
import requests
import json
import os

# #https://download1518.mediafire.com/pjbmrxu3fyig/ygh79hofhj9npol/config.json
dir_path = os.path.dirname(os.path.realpath(__file__))

def download(url, filename, callback):
    print(Fore.GREEN)
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
        callback('error')
    callback('successful')


def ondownload(state):
    if state == "successful":
        print(f'{Fore.GREEN}[ABYSS-INFO]:config.json file downloaded.')
        print(f'{Fore.GREEN}[ABYSS-INFO]: Please run again the file.')
    else:
        print(f'{Fore.GREEN}[ABYSS-ERROR]: Error downloading config.json file, check your iternet connection or try again.')
    exit() 


class Abyss:
    
   
        def __init__(self):
            self.foreground = None
            self.background = None
            self.error_color = None
            self.Info_color = None
            self.title_font = None
            self.title = None
            self.subtitle = None

        def init(themename,path,filename):
            try:
                f = open(f'{path}/{filename}', 'r')
                c = f.read()
                js = json.loads(c)
                
                foreground = js[themename]['style']['foreground'].upper()
                background = js[themename]['style']['background'].upper()
                error_color = js[themename]['style']['error_color'].upper()
                info_color = js[themename]['style']['info_color'].upper()
                title_font = js[themename]['style']['title_font'].upper()

                title = js[themename]['shell_info']['title'].upper()
                subtitle = js[themename]['shell_info']['subtitle'].upper()

                foreground = getattr(Fore, foreground)
                background = getattr(Fore, background)
                error_color = getattr(Fore, error_color)
                info_color = getattr(Fore, info_color)

                build(Abyss,foreground,error_color,info_color,background,title_font,title,subtitle)

            except FileNotFoundError:
                print(f'{Fore.RED}[ABYSS-ERROR]:File config.json not found.')
                print(f'{Fore.GREEN}[ABYSS-INFO]: Downloading config.json file...')
                download('https://drive.google.com/u/0/uc?id=15hGFtFkaupcuzcpJYdU5vmLmZwK5pywz&export=download',
                f'{path}/{filename}', ondownload)
        
        def generate_menu(options):
            option = None
            options[f'{len(options)+1}']=('salida', exitmenu)
            while option != len(options):
                show_menu(options)
                option = read_option(options)
                run(option, options)

def show_menu(options):
    print('Seleccione una opción:')
    for i in sorted(options):
        print(f' {i}) {options[i][0]}')

def read_option(options):
    while (a := input('Opción: ')) not in options:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def run(option, options):
    options[option][1]()

def exitmenu():
    print('Exiting')
    exit()

def build(self,foreground=Fore.BLACK, error_color=Fore.BLUE, info_color=Fore.CYAN, background='f0', title_font="wavy",title="ABYSS",subtitle="Shell Library, KAT"):
    self.foreground = foreground
    self.background = background
    self.error_color = error_color
    self.Info_color = info_color
    self.title_font = title_font
    self.title = title
    self.subtitle = subtitle
    cleanScreen()
    title = pyfiglet.figlet_format(title, font = title_font)
    print(foreground)
    print(title)
    print(subtitle)


def cleanScreen():
    _  = system('cls')