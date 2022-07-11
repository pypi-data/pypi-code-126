# GPSDO Nextion version
import serial                    # Py serial use pip3 to install
import serial.tools.list_ports   # Py serial tools use pip3 to install - used to find current USB port
import os
from time import sleep           # used to catch up on rest after a hard day
from threading import Thread, Lock     # used to create program threads
import shelve 
## getFreq.py code from ubxpoller.py Created on 2 Oct 2020 @author: semuadmin
getFreq = True    # set to False to switch off receiver frequency check (polly) 

device='/dev/ttyUSB0'         # this is the Nextion screen device - the program will track changes in the USB number
device2='/dev/ttyS0'          # this is the GPS device. 
display=(True)  # Locked so OK to write to the Nextion display

# variables set frequencies if not using the display
# leave at default settings 
unF =10         # unlocked frequency Hz
loF =1000000    # GPS locked frequency Hz
unDC=10         # unlocked duty cycle %   
loDC=50         # locked duty cycle %  
time="0"
date="0"
terminator = b'\xff\xff\xff'  # used to terminate every command
quote=b"\x22"                 # used to encase strings in quotes
lockStatus=(False)
reading = False

class Nextion:
   def __init__(self):
        self.ser = serial.Serial(device, 38400, timeout=1)

   def connect(self):
       self.ser.write(b"connect" + terminator)
       r = self.ser.read(128)
       return r

   def get(self,command):
       self.ser.write(command.encode() + terminator)
       raw = self.ser.readline()
       if raw is not None:
          # convert bytearray to string
          data = "".join([chr(b) for b in raw])
          return data
       else:
          return 0

   def set(self,command, var):
       self.ser.write(command.encode() + quote + var.encode() +quote + terminator)

##################################
class GPS:
   def __init__(self):
        self.gps = serial.Serial(device2, 9600, timeout=0.1)

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


  
####################### reads and updates the Nextion display
def getData():
  print("running getData()")
  while True:
      global unF,unDC,loF,loDC,lockStatus,display,time,date
      op=n.get("get page1.output.txt")
      parts = op.split(",")
      if op=="":
         continue
      #print(parts)
      #print(parts[1],parts[2],parts[3],parts[4])
      if(parts[1]=="1"):  # set locked frequency
          #print(parts[1],parts[2],parts[3],parts[4])
          loF=int(parts[4])
          if(loF<11999999 and loF>0):
            loDC=int(parts[3])
            if(display):
               display=(False) # stops unlocked() sub writing to screen
               n.get("page 0")
               #sleep(0.5)
               n.set("page0.t3.txt=","writing to GPS")
               #sleep(0.5)
               write(unF,unDC,loF,loDC)
               print("GPS module updated")
               print("Locked frequency = "+str(loF)+" Hz")
               print("Locked duty cycle = "+str(loDC)+" %")
               print("Unlocked frequency = "+str(unF)+" Hz")
               print("Unlocked duty cycle = "+str(unDC)+" %\n")
               #sleep(0.5)
               n.set("page0.t2.txt=",str(loF)+" Hz")   
               #sleep(0.5)
               n.set("page0.t3.txt=",str(unF)+" Hz")   
               display=(True)
            else:
               write(unF,unDC,loF,loDC)
      if(parts[2]=="1"):  # set unlocked frequency
          #print("Command "+parts[1],parts[2],parts[3],parts[4])
          unF=int(parts[4])
          if(unF<11999999 and unF>0):
            unDC=int(parts[3])
            if(display):
               display=(False) # stops unlocked() sub writing to screen
               n.get("page 0")
               sleep(0.5)
               n.set("page0.t3.txt=","writing to GPS")
               sleep(0.5)
               write(unF,unDC,loF,loDC)
               print("GPS module updated")
               print("Locked frequency = "+str(loF)+" Hz")
               print("Locked duty cycle = "+str(loDC)+" %")
               print("Unlocked frequency = "+str(unF)+" Hz")
               print("Unlocked duty cycle = "+str(unDC)+" %\n")
               sleep(0.5)
               n.set("page0.t2.txt=",str(loF)+" Hz")   
               sleep(0.5)
               n.set("page0.t3.txt=",str(unF)+" Hz")   
               display=(True)
            else:
               write(unF,unDC,loF,loDC)
      
      # display the time, date and lock status  
      if(display):
         n.set("page0.time.txt=",time+" UTC")
         n.set("page0.t1.txt=",date+" UTC")  
         n.set("page0.t2.txt=",str(loF)+" Hz")   
         n.set("page0.t3.txt=",str(unF)+" Hz")     
         if(lockStatus):
            n.set("page0.t0.txt=","GPS Locked")
         else:
            n.set("page0.t0.txt=","GPS Not Locked")

  
###################### this finds the acive USB port numer which will increment every time the USB dongle is plugged in. It resets to USB0 on reboot
def checkUSB():
   global device
   myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
   #print (myports)
   bob=str(myports[0:1])
   device=(bob[3:15])
   if(device=="/dev/ttyAMA0"):
     print("USB device error - reboot")
     #If the terminal reports dev/ttyAMA0 the serial USB device is not working
   print(device)


######################
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
   print("\nLocked frequency = "+str(loF)+" Hz")
   print("Locked duty cycle = "+str(loDC)+" %")
   print("Unlocked frequency = "+str(unF)+" Hz")
   print("Unlocked duty cycle = "+str(unDC)+" %\n")

#######################
def main():                 
   print("Starting Threads")
   t1=Thread(target=locked)
   t2=Thread(target=getData)
   t1.start()
   sleep(1)
   t2.start()
   print("Time = "+time)
   print("Date = "+date+"\n")
#######################
checkUSB()
n=Nextion()
g=GPS()
if(getFreq):
   polly()
main()



