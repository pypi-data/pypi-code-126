import requests

from .Demotivator import Demotivator
from .Quote import Quote

try:
    version = requests.get(
        'https://codeberg.org/Daemon-RE/openre-pylib/raw/branch/main/orpl/version.txt'
    ).text.splitlines()

    if version[0] != '1.0':
        print(f'[OpenREPYLib] Данная версия библиотеки устарела, обновитесь до v{version[0]} с GitHub',
              f'\nИзменения: {version[1]}')
except requests.exceptions.RequestException:
    print('[OpenREPYLib] Не удалось проверить версию библиотеки на актуальность')

__all__ = (
    'Demotivator',
    'Quote'
)
