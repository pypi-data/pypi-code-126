import webbrowser #import webbrowser to open the urls
import pyautogui #import pyauto gui to do the typing
import time #imports time for delays

def webdmclose(number, message): #Defines the usage of the libary and allows the input of the number and message
    webbrowser.open(f"https://web.whatsapp.com/send?phone={number}&text={message}") #Opens whatsapp web to send message with adding the variables that the user provided
    time.sleep(12) #Waits for the link to be opened
    pyautogui.press('enter') #Presses enter to send the message
    time.sleep(2) #Waits 2 seconds for wifi delay and to let the user see the message
    pyautogui.hotkey('ctrl', 'w') #Closes the whatsapp web tab

def webdmkeepopen(number,message): #Defines the usage of the libary and allows the input of the number and message
    webbrowser.open(f"https://web.whatsapp.com/send?phone={number}&text={message}") #Opens whatsapp web to send message with adding the variables that the user provided
    time.sleep(12) #Waits for the link to be opened
    pyautogui.press('enter') #Presses enter to send the message

def phonedm(number, message):  #Defines the usage of the libary and allows the input of the number and message for phone
    webbrowser.open(f"https://wa.me/{number}/?text={message}") #Opens the phone whatsapp api url to make it redirect the app to send the message
    #Will implement auto sending later

def phonegroup(): # Defines the usage of a libary that I am yet to figure out how to use.
    print("Will be added later once I figure out how to implement it") #Just here to print if someone accidently runs it.

def webgroupclose(invite, message): #Defines the usage of the libary and allows the input of the number and message
    webbrowser.open(f"https://web.whatsapp.com/accept?code={invite}") #Opens whatsapp web to send message with adding the variables that the user provided
    time.sleep(15)#Waits for the link to be opened
    pyautogui.write(message)#Writes the message
    pyautogui.press('enter')#Presses enter to send the message
    time.sleep(2)#Waits 2 seconds for wifi delay and to let the user see the message
    pyautogui.hotkey('ctrl', 'w')#Closes the whatsapp web tab

def webgroupopen(invite, message): #Defines the usage of the libary and allows the input of the number and message
    webbrowser.open(f"https://web.whatsapp.com/accept?code={invite}") #Opens whatsapp web to send message with adding the variables that the user provided
    time.sleep(15) #Waits for the link to be opened
    pyautogui.write(message) #Writes the message
    pyautogui.press('enter') #Presses enter to send the message