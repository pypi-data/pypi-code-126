import sys
from typing import overload
import atexit
import random

def exit_handler():
    sys.stdout.write("\033[?25h")
atexit.register(exit_handler)


def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return [v, v, v]
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    v=int(v)
    p=int(p)
    t=int(t)
    if i == 0: return [v, t, p]
    if i == 1: return [q, v, p]
    if i == 2: return [p, v, t]
    if i == 3: return [p, q, v]
    if i == 4: return [t, p, v]
    if i == 5: return [v, p, q]

def loadingNotSmooth(perc : float, frase : str = '' ) -> None:
    if not isinstance(perc, float):
        raise TypeError(f"perc must be a float between 0 and 1")
    if perc<0:
        perc=0
    if perc>1:
        perc=1
    maxo=80

    num=int(perc*maxo)
    resto=perc*maxo-num
    meni=""
    for i in range(num):
        meni+=color("█",hsv_to_rgb(i/maxo,1,1))
    stri="|"+meni+" "*int(maxo-num)+"|"+str(int((perc*1000)//1)/10)+"% "+frase
    printo(stri)

def loading(perc : float, frase : str = '' ) -> None:
    if not isinstance(perc, float):
        raise TypeError(f"perc must be a float between 0 and 1")
    if perc<0:
        perc=0
    if perc>1:
        perc=1
    maxo=80
    num=int(perc*maxo)
    resto=perc*maxo-num
    resti=['','▏','▎','▍','▌','▋','▊','▉']
    resto=int(resto*len(resti))


    meni=""
    for i in range(num):
        meni+=color("█",hsv_to_rgb(i/maxo,1,1))
    i=num
    meni+=color(resti[resto],hsv_to_rgb(i/maxo,1,1))
    if not resto==0:
        num=num+1
    stri="|"+meni+" "*int(maxo-num)+"|"+str(int((perc*1000)//1)/10)+"% "+frase
    printo(stri)



def printo(obj,colore: list[int]=[255,255,255]) -> None:
    sys.stdout.write(f"\r{color(obj,colore)}")
    sys.stdout.flush()
    sys.stdout.write("\033[?25l")
    sys.stdout.write("\033[K")


def deleteLastLine() -> None:
    
    sys.stdout.write("\033[K")   
    sys.stdout.write("\r")
    sys.stdout.flush()


def bites(byt: int, cifre : int = 2) -> str:
    siz=['b','Kb','Mb','Gb','Tb']
    cont=0
    while(byt>1024):
        byt=byt/1024
        cont=cont+1
    return f"{format(byt,f'.{cifre}f')}{siz[cont]}"
    

@overload
def color(string: str, colore: int) -> str:
    ...
@overload
def color(string: str, colore: list[int]) -> str:
    ...
def color(string: str, colore) -> str:
    if isinstance(colore, int):
        if colore>7 or colore<0:
            raise TypeError(f"color must be between 0 and 7")
        return f"\033[9{colore}m{string}\033[0m"
    elif isinstance(colore, list):
        if len(colore)!=3:
            raise TypeError(f"color must have len=3")

        for a in colore:
            if not isinstance(a, int):
                raise TypeError(f"color must be a list[int]")
            if a>255 or a<0:
                raise TypeError(f"color every element of color must be between 0 and 255")

        return f"\x1b[38;2;{colore[0]};{colore[1]};{colore[2]}m{string}\x1b[0m"
    else:
        raise TypeError(f"color must be int or list[int] with len 3 but is {type(color)}")

def scolor(colore: int):
    return f"\033[9{colore}m"
#endc = "\033[0m"

def randomVividColor() -> float:
    return hsv_to_rgb(random.random(),1.,1.)
