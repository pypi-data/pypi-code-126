import time
import requests, os
os.system('pip install httpx')
import httpx
httpx4 = httpx.session()
class Main():
  def old(msg):
    for char in msg:
      print(char, end='')
      time.sleep(0.09)
  def new(msg):
    rt = str(len(msg))
    return rt 
class test():
  def tstg(url):
    ty = httpx4.get(url).content
    return ty