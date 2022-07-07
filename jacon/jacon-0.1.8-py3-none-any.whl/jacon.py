import time
import requests, os
try:
  import httpx
except ImportError:
  os.system('pip install httpx')
import httpx
httpx4 = httpx.Client()
class Main():
  def old(msg):
    for char in str(msg):
      print(char, end='')
      time.sleep(0.09)
  def new(msg):
    rt = str(len(msg))
    return rt 
class test():
  def tstg(url):
    ty = httpx4.get(url).content
    return ty

def get():
  