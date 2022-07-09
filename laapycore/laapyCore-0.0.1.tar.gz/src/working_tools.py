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
