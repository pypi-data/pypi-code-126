#code created by daniel kenan slinda
from os import system as terminal
from sys import platform
from random import randint  as num
coords = [["  " for content in range(0, 10)] for num_row in range(0, 10)]
os = None

def system():
    global os
    game.clear()

class Minesweeper:

     def clear(self):
        
         terminal("clear")

     @property
     def Interface(self):

        print("        0  1  2  3  4  5  6  7  8  9")
    

        def buffer(board):
              space_before,container = "     ","_"*31
              print(space_before,container,"\n")
              board()
              print(space_before,container)

        @buffer
        def board():
         for row_draw in range(0,10):
                    print(f"  {row_draw}   |","|".join(coords[row_draw]),"|",sep="")

     @property
     def explosives(self):
       positions = []
       [positions.append([i]+[num(0,9)]) for i in range(0,9)]
       return positions
     @property
     def error(self):
         raise ZeroDivisionError

if __name__ == "__main__":
  game = Minesweeper()
  explosives = game.explosives
  #print(explosives)

  print("welcome to minesweeper \n\n")

  def gameplay():
    try:
        while True:
           game.Interface
           user = input("input a row and column: ").strip().split()
           check = None if [int(user[0])]+[int(user[1])] not in explosives else game.error
           coords[int(user[0])][int(user[1])] = " X"
           system()

    except ZeroDivisionError:
        arr = explosives
        all_rows  = [i[0] for i in arr]
        all_columns = [i[1] for i in arr]
        i = 0
        while i < len(arr):
            coords[all_rows[i]][all_columns[i]] = " 0"
            i += 1
        system()
        game.Interface
        print("\n\t\tgame over!!!")
    except:
        system()
        gameplay()