#!/usr/bin/env python3

from fire import Fire
import math

import numpy as np
import matplotlib.pyplot as plt


# https://en.wikipedia.org/wiki/Erlang_distribution#/media/File:Erlang_dist_cdf.svg
#num = input("Enter a number: ")
#print("The factorial of ", num, " is : ")
#print(math.factorial(int(num)))


def erlang_cum(x,rate,k=1):
    # in the test - i supply:   1/mu == rate
    res = 0
    for n in range(k):
        res+=1/math.factorial(int(n)) * np.exp(-rate*x)*np.power(x*rate,n)
        #print(f"                 n={n},  {res}")
        #res=math.exp(-rate*x)
    return 1 - res


def main():
    print("Erlang_cum for rate 85000 at 8us:", erlang_cum(8e-6, 85000, 1) ," " )
    print("Erlang_cum for rate 85000 at 4.5us:", erlang_cum(4.5e-6, 85000, 1) ," " )
    print("Erlang_cum for rate 85000 at 0.4us:", erlang_cum(0.4e-6, 85000, 1) ," " )


    print("Erlang test image")
    x = np.linspace(0,20,50)

    y = erlang_cum( x, 1/2, 1 )
    plt.plot(x,y,'r-')

    y = erlang_cum( x, 1/1, 9 )
    plt.plot(x,y,'b-')

    y = erlang_cum( x, 1/1, 1 )
    plt.plot(x,y,'m-')

    y = erlang_cum( x, 1/0.5, 7 )
    plt.plot(x,y,'k-')

    y = erlang_cum( x, 1/2, 3 )
    plt.plot(x,y,'y-')

    y = erlang_cum( x, 1/1, 5 )
    plt.plot(x,y,'g-')

    y = erlang_cum( x, 1/2, 2 )
    plt.plot(x,y,'-', color='orange')

    plt.margins(0.005, tight=True)
    plt.grid(True)
    plt.show()


    # for x in np.arange(0, 1.2,  0.2):
    #     print(f"{x:.1f}  (rate={rate})", erlang(x,rate))

if __name__=="__main__":
    Fire(main)
