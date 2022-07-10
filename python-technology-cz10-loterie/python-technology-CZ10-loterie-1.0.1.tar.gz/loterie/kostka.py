import random
import time

# dokumentace: https://github.com/rsalmei/alive-progress
from alive_progress import alive_bar


def hod_kostkou():
    return random.randint(1, 6)


def hod_kostkou_s_progress_barem(popisek_hodu, delka_hodu_v_sekundach):
    hozene_cislo = hod_kostkou()

    # vykresleni progress baru pomoci kontext manazeru (with konstrukce)
    with alive_bar(delka_hodu_v_sekundach * 100, title=popisek_hodu, stats=False,
                   elapsed=False, bar="filling") as bar:
        # pokud nepouzivame promennou, tak je konvence ji pojmenovat '_'
        # cely nas progress bar ma pocet dilku = delka_hodu_v_sekundach * 100
        # jeden dilek je vykreslen volanim funkce bar() a mezi kazdym vykreslenim chceme cekat 0.01 sekund
        for _ in range(delka_hodu_v_sekundach * 100):
            time.sleep(0.01)
            bar()

    return hozene_cislo
