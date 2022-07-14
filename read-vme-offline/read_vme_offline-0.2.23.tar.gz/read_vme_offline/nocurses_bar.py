#!/usr/bin/env python3

from fire import Fire
import datetime as dt
import time

import pytermgui
from pytermgui import print_to, report_cursor, bold, inverse, underline, italic, save_cursor, restore_cursor, terminal, cursor_up, move_cursor


import threading # for key input

theight= terminal.height
twidth= terminal.width


global_mode = " "

from console import fg, bg, fx

class Topbar:
    def __init__(self, pos=1 ):
        self.pos = pos
        self.positions = {}
        self.t2 = None
        if pos==1:
            self.BCOL = bg.cyan
        elif pos==2:
            self.BCOL = bg.white

        #print( pos, report_cursor() )
        #print( pos, report_cursor() )
        #print( pos, report_cursor() )
        try:
            print("report_cursor to appear")
            print( pos, report_cursor() )
            print("report done")
        except:
            print("X... problem with report_cursor")

        print("i... nocurses bar started")

    def add(self,two):
        if two==2:
            self.t2 = Topbar(two)
        return self.t2


    def print_to(self, tup, s):
        self.positions[ tup[0] ] = s
        #if self.pos==1: save_cursor()
        #print_to( tup, s )
        #if self.pos==1: restore_cursor()

    def place(self):

        #self.BCOL = bg.cyan
        #if self.pos==2: self.BCOL=bg.lightwhite
        curs =(-1,-1)
        if self.pos==1:
            save_cursor()
        #     try:
        #         curs = report_cursor() # mess in printing
        #     except:
        #         curs=(-1,-1)

        #print_to( (1,1), inverse(colored(" "*twidth ,"cyan") ) )
        print_to( (1,self.pos),  f"{self.BCOL}"+" "*twidth+bg.default )
        print_to( (1,self.pos+1), " "*twidth )

        for k in self.positions.keys():
            #print(f"i... {k}")
            #print_to( (k,1), " "*twidth)
            print_to( (k,self.pos), f"{self.BCOL}{self.positions[k]}{bg.default}" )

        # DEBUG CURSOR
        #print_to( (1,self.pos), f"{bg.magenta}{curs}{bg.default}" )

        if self.t2 is not None:
            self.t2.place()

        if self.pos==1:
            restore_cursor()
            #if not curs is None:
            #    if curs[0]>0:move_cursor( curs)
            #report_cursor() # this makes a mess in printing
            print("", end="\r") # this make GOOD thing in printing
            #print("", end="") # NOT ENOUGH  GOOD printing
        #print(curs)






def my_callback(inp):
    """
    Read input + enter from keyboard. In the thread.
    """
    global global_mode
    print(f'You Entered: /{inp}/;  valid=r:s' , flush = True)
    if inp=='r':
        global_mode = 'r'
    if inp=='s':
        global_mode = 's'
    #time.sleep(2)






#--------https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
# ON ENTER
# CALL WITH CALLBACK FUNCTION AS A PARAMETER
class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk = None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        self.block = False
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            time.sleep(0.02)
            self.input_cbk(input()) #waits to get input + Return

    def pause(self):
        self.block = True

    def unpause(self):
        self.block = False




def main():


    t = Topbar(1)
    print("topbar 1 defined")
    t2 = t.add(2)
    print("topbar 2 defined")


    #start the Keyboard thread AFTER TOPBAR
    print("preparing kthread")
    kthread = KeyboardThread(my_callback)
    print("kthread defined")


    for i in range(1000):
        t.place()
        if (i<10) or (global_mode == 'r'):
            t.print_to((1,  1), f'{fg.white}{fx.bold}{dt.datetime.now()}{fg.default}'  )
            t.print_to((30, 1),  f'{fg.lightblack}lighbl{fg.default}' )
            t.print_to((40, 1),  f'{fg.lightwhite}lighwhite{fg.default}' )
            t.print_to((50, 1),  f'{fg.black}BLASCK{fg.default}')
            t.print_to((60, 1),  f'{fg.black}{bg.yellow}BLASCK{bg.default}{fg.default}')

            t2.print_to((1,  2), f'{fg.black}{dt.datetime.now()}{fg.default}' )
            t2.print_to((30,  2), f'{fg.black}{bg.red}red{bg.default}{fg.default}' )
        t2.print_to((50,  2), f'MODE:{fg.black}{bg.yellow}{global_mode}{bg.default}{fg.default}' )

        time.sleep(0.1)
        print(f"i... ahoj {i}")




if __name__=="__main__":
    Fire(main)
