"""
ubxpoller.py
This example illustrates a simple implementation of a
'pseudo-concurrent' threaded UBXMessage configuration
polling utility.
(NB: Since Python implements a Global Interpreter Lock (GIL),
threads are not truly concurrent.)
It connects to the receiver's serial port and sets up a
UBXReader read thread. With the read thread running
in the background, it sends a variety of CFG POLL
messages to the device. The read thread reads and parses
any responses to these polls and outputs them to the terminal.
The response may be an ACK-ACK acknowledgement message followed
by the poll response itself, or an ACK-NAK message signifying
that this particular configuration message type is not supported
by the receiver.
Created on 2 Oct 2020
@author: semuadmin
"""
# pylint: disable=invalid-name

from sys import platform
from io import BufferedReader
from threading import Thread, Lock
from time import sleep
from serial import Serial
from pyubx2 import (
    UBXMessage,
    UBXReader,
    POLL,
    UBX_MSGIDS,
)
import shelve 
# initialise global variables
reading = False
aData="Not full yet"


def read_messages(stream, lock, ubxreader):
    global aData
    """
    Reads, parses and prints out incoming UBX messages
    """
    # pylint: disable=unused-variable, broad-except

    while reading:
        if stream.in_waiting:
            try:
                lock.acquire()
                (raw_data, parsed_data) = ubxreader.read()
                lock.release()
                if parsed_data:
                    #print(parsed_data)
                    aData=(str(parsed_data))
                    parts = aData.split(",")
                    #print()
                    f1=int((parts[6])[12:]) 
                    #print("Unlocked frequency = "+str(f1)+" Hz")
                    f2=int((parts[7])[16:]) 
                    d1=float((parts[8])[15:])/42949673.00 
                    d1=round(d1)
                    #print("Unlocked duty cycle = "+str(d1)+" %")
                    d2=float((parts[9])[19:])/42949673.00 
                    d2=round(d2)
                    #print("Locked frequency = "+str(f2)+" Hz")
                    #print("Locked duty cycle = "+str(d2)+" %")
                    outfile = shelve.open("myfile") 
                    outfile["unF"] = f1 
                    outfile["unDC"] = d1
                    outfile["loF"] = f2 
                    outfile["loDC"] = d2 
                    return 
                    
            except Exception as err:
                print(f"\n\nSomething went wrong {err}\n\n")
                continue


def start_thread(stream, lock, ubxreader):
    """
    Start read thread
    """

    thr = Thread(target=read_messages, args=(stream, lock, ubxreader), daemon=True)
    thr.start()
    return thr


def send_message(stream, lock, message):
    """
    Send message to device
    """

    lock.acquire()
    stream.write(message.serialize())
    lock.release()

if __name__ == "__main__":

    # set port, baudrate and timeout to suit your device configuration
    if platform == "win32":  # Windows
        port = "COM13"
    elif platform == "darwin":  # MacOS
        port = "/dev/tty.usbmodem14101"
    else:  # Linux
        port = "/dev/ttyS0"
    baudrate = 9600
    timeout = 0.1

    with Serial(port, baudrate, timeout=timeout) as serial:

        # create UBXReader instance, reading only UBX messages
        ubr = UBXReader(BufferedReader(serial), protfilter=2)

        print("\nStarting UBX read thread...\n")
        reading = True
        serial_lock = Lock()
        read_thread = start_thread(serial, serial_lock, ubr)

        # poll all available CFG configuration messages
        #print("\nPolling CFG configuration CFG-*...\n")
        msg = UBXMessage("CFG", "CFG-TP5", POLL)
        send_message(serial, serial_lock, msg)
        #sleep(1)
        #print("\nPolling complete. Pausing for any final responses...\n")
        sleep(1)
        #print("\nStopping reader thread...\n")
        reading = False
        read_thread.join()
        print("Processing Complete\n")
        
