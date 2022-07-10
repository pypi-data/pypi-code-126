from .libs import *
from .constants import *


def step(x): return np.heaviside(x, 1)
def rect(x): return np.where(abs(x) <= 0.5, 1, 0)


def sin(x, n=1, symp=1): return sym.sin(x)**n if symp else np.sin(x)**n


def cos(x, n=1, symp=1): return sym.cos(x)**n if symp else np.cos(x)**n


def tan(x, n=1, symp=1): return sym.tan(x)**n if symp else np.tan(x)**n


def sec(x, n=1, symp=1): return sym.sec(x)**n if symp else (1/np.cos(x))**n


def csc(x, n=1, symp=1): return sym.csc(x)**n if symp else (1/np.sin(x))**n


def cot(x, n=1, symp=1): return sym.cot(x)**n if symp else (1/np.tan(x))**n


def abccos(x, a, p, f=np.pi, d=0): return a*np.cos(x*f+p)+d


def abcsin(x, a, p, f=np.pi, d=0): return a*np.sin(x*f+p)+d


'''
Math Functions
'''


def tet(base, n, num=None):  # funksjon for å eksponere med seg selv i rekke
    if not num:
        num = base
    if n == 0:
        return base
    else:
        return tet(num**base, n-1, num=num)


def abc(a, b, c):
    rot = (b**2-4*a*c)**.5
    return ((b+rot)/(2*a), (b-rot)/(2*a))


def symabc(a, b, c):
    rot = sym.sqrt(b**2-4*a*c)
    return ((-b+rot)/(2*a), (-b-rot)/(2*a))


def polar2cart(r, theta, rad=True):
    if not rad:
        theta *= np.pi/180
    return r*(np.cos(theta) + 1j*np.sin(theta))


def cart2polar(A: Union[int, np.complex128], B: int = 0, rad=True):
    if type(A) in [np.complex128, complex]:
        B = A.imag
        A = A.real
    r = (A**2+B**2)**.5
    theta = np.pi/2 if A == 0 else np.arctan(B/A)+(A < 0)*np.pi
    return r, theta if rad else theta*180/np.pi


def integrate(exp, var, degree=1):
    while (degree > 0):
        exp = sym.integrate(exp, var, conds='none')
        degree -= 1
    return exp


def pythagoranTri(m, n):
    a = 2*m*n
    b = m**2-n**2
    c = m**2+n**2
    return a, b, c


def pythagoranQuad(m, n, p, q):
    a = m**2 + n**2 - p**2 - q**2
    b = 2*(m*q+n*p)
    c = 2*(n*q-m*p)
    d = m**2 + n**2 + p**2 + q**2

    return a, b, c, d
