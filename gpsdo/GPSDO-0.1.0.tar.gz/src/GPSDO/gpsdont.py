# GPSDO No Terminal version
import serial                    # Py serial use pip3 to install
import serial.tools.list_ports   # Py serial tools use pip3 to install - used to find current USB port
from time import sleep           # used to catch up on rest after a hard day
import os
import sys
import shelve 
from threading import Thread     # used to create program threads
## getFreq.py code from ubxpoller.py Created on 2 Oct 2020 @author: semuadmin
getFreq = True    # set to False to switch off receiver frequency check (polly) 

device2='/dev/ttyS0'          # this is the GPS device. 

# These variables are defaults don't change them 
unF =10         # unlocked frequency Hz
loF =1000000    # GPS locked frequency Hz
unDC=10         # unlocked duty cycle %   
loDC=50         # locked duty cycle %  
time="0"
date="0"
terminator = b'\xff\xff\xff'  # used to terminate every command
quote=b"\x22"                 # used to encase strings in quotes
lockStatus=(False)

##################################
class GPS:
   def __init__(self):
        self.gps = serial.Serial(device2, 9600, timeout=1)

   def getGPS(self):
       raw = self.gps.readline()
       return raw

   def setGPS(self,command):
       self.gps.write(command)

   def pollGPS(self):
       raw = self.gps.read(44)
       return raw
   
       
##########################################
def write(unF,unDC,loF,loDC):
        # Save frequencies 
        excel = [181,98,6,49,32,0,0,1,0,0,0,0,0,0,1,0,0,0,0,18,122,0,154,153,153,25,0,0,0,128,0,0,0,0,111,0,0,0,185,98]
        mod=excel.copy()
        code=getCode(mod,unF,unDC,loF,loDC)
        pl=code.copy()
        pl=pl[2:38]
        payload = bytearray(pl)
        payloadLength = int.from_bytes(payload[2:4], byteorder='little', signed=False)
        #print("payload length ",payloadLength)

        check=getChecksum(payload)   # calculate the new checksum and add it to the byte string
        #print(check[0],check[1])
        code[38]=check[0]
        code[39]=check[1]
        #print(excel)
        #print(code)
        msg= g.setGPS(code)
        # save the new frequency to Eprom
        save=[181,98,6,9,13,0,0,0,0,0,255,255,0,0,0,0,0,0,3,29,171]
        #ck1=[6,9,13,0,0,0,0,0,255,255,0,0,0,0,0,0,17]
        #check=getChecksum(ck1)
        #print(check[0],check[1])
        #print(save)
        msg= g.setGPS(save)

##########################################
def getCode(excel,unF,unDC,loF,loDC):
    output=[0]*32
    vHex="0x%0.6X" % unF         # unlocked frequency
    #print("unlocked "+vHex)
    #print()
    byte2="0x"+vHex[2:4]
    byte1="0x"+vHex[4:6]
    byte0="0x"+vHex[6:8] 
    excel[14]=int(byte0,16)
    excel[15]=int(byte1,16)
    excel[16]=int(byte2,16)

    vHex="0x%0.6X" % loF         # locked frequency
    #print("locked "+vHex)
    byte2="0x"+vHex[2:4]
    byte1="0x"+vHex[4:6]
    byte0="0x"+vHex[6:8]
    excel[18]=int(byte0,16)
    excel[19]=int(byte1,16)
    excel[20]=int(byte2,16)

    unPC=int((unDC/100)*4294967295)    # unlocked duty cycle
    vHex="0x%0.8X" % unPC
    byte3="0x"+vHex[2:4]
    byte2="0x"+vHex[4:6]
    byte1="0x"+vHex[6:8]
    byte0="0x"+vHex[8:10]
    excel[22]=int(byte0,16)
    excel[23]=int(byte1,16)
    excel[24]=int(byte2,16)
    excel[25]=int(byte3,16)

    loPC=int((loDC/100)*4294967295*1.003)   # locked duty cycle
    vHex="0x%0.8X" % loPC 
    byte3="0x"+vHex[2:4]
    byte2="0x"+vHex[4:6]
    byte1="0x"+vHex[6:8]
    byte0="0x"+vHex[8:10]
    excel[26]=int(byte0,16)
    excel[27]=int(byte1,16)
    excel[28]=int(byte2,16)
    excel[29]=int(byte3,16)
    #print(loDC/100,unDC/100)
    #print()
    return excel
#########################################
def getChecksum(packet):
     """Calculate a combined Checksum for the given bytestrings."""
     CK_A = 0
     CK_B = 0
     for i in range(len(packet)):
        CK_A = CK_A + packet[i]
        CK_B = CK_B + CK_A    
     CK_A = CK_A & 0xFF
     CK_B = CK_B & 0xFF
     check=[CK_A,CK_B] 
     return check
###################### Find if GPS is locked and return the time
def locked():
   global time,date,lockStatus
   print("running locked()")
   while True:
      try:
        byteData = g.getGPS()
      except:
        print("exception")
        print("loop")
        return 0
      if byteData is not None:
        # convert bytearray to string
        data = "".join([chr(b) for b in byteData])
        vMessage = data[0:6]
        if (vMessage == "$GPRMC" or vMessage == "$GNRMC"):   # Get the position data that was transmitted with the GPRMC message
             parts = data.split(",")
             #print(data) # used for debug
             valid=parts[2]
             if(valid=="A"):
                lockStatus=(True)
             else:
                lockStatus=(False)
             vtime=parts[1]
             hrs=vtime[0:2]
             mins=vtime[2:4]
             secs=vtime[4:6]
             time=hrs+":"+mins+":"+secs
             vdate=parts[9]
             dd=vdate[0:2]
             mm=vdate[2:4]
             yy=vdate[4:6]
             date=dd+"/"+mm+"/"+yy


  
#######################
# gets current frequency status and displays it
def polly(): 
   global unF,unDC,loF,loDC
   # Get current GPS frequency status from test.py
   aData=os.system("python getFreq.py arg1 arg2")  
   infile = shelve.open("myfile") 
   #print(infile["unF"], infile["unDC"], infile["loF"], infile["loDC"]) 
   unF=int(infile["unF"])
   unDC=(infile["unDC"])
   loF=infile["loF"]
   loDC=(infile["loDC"])

#######################
def main():                 
   global unF,unDC,loF,loDC
   print("Starting Threads")
   t1=Thread(target=locked)
   t1.start()
   sleep(1)
   print("Time = "+time)
   print("Date = "+date)
   print()
   print("\nLocked frequency = "+str(loF)+" Hz")
   print("Locked duty cycle = "+str(loDC)+" %")
   print("Unlocked frequency = "+str(unF)+" Hz")
   print("Unlocked duty cycle = "+str(unDC)+" %\n")
   print("Enter Q to quit")
   text1 = input("Enter new locked frequency in Hz or <Enter> ")
   if(text1=="q" or text1=="Q"):
     return
   if(text1!=""):
     loF=int(text1)
     if(loF>11000000):
       loF=11000000 
     if(loF<1):
       loF=1 
   print(str(loF)+" Hz") 
   
   text2 = input("Enter new locked duty cycle in % or <Enter> ")
   if(text2=="q" or text2=="Q"):
     return
   if(text2!=""):
     loDC=int(text2)
     if(loDC>90):
       loDC=90 
     if(loDC<10):
       loDC=10 
   print(str(loDC)+" %") 
 
   text3 = input("Enter new unlocked frequency in Hz or <Enter> ")
   if(text3=="q" or text3=="Q"):
     return
   if(text3!=""):
     unF=int(text3)
     if(unF>11000000):
       unF=11000000 
     if(unF<1):
       unF=1 
   print(str(unF)+" Hz") 

   text4 = input("Enter new unlocked duty cycle in % or <Enter> ")
   if(text4=="q" or text4=="Q"):
     return
   if(text4!=""):
     unDC=int(text4)
     if(unDC>90):
       unDC=90 
     if(unDC<10):
       unDC=10 
   print(str(unDC)+" %") 
   print("\nWriting to the GPS module")
   write(unF,unDC,loF,loDC)
   print("\nAll done. Exiting now.\n")
   return

#######################
g=GPS()
if(getFreq):
   polly()
main()
os._exit(1) 


