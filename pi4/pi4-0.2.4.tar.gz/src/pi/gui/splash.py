'''
Demo: show splash screen before loading main GUI
'''

from tkinter import *
from PIL import ImageTk,Image
from pathlib import Path

#SplashScreen

sroot = Tk()

W = sroot.winfo_screenwidth()
H = sroot.winfo_screenheight()

# sroot.minsize(height=200,width=300)
#Adding transparent background property
# sroot.wm_attributes('-transparentcolor', '#000000')
sroot.attributes('-fullscreen', True)
sroot.title("Splash window")
sroot.configure()
spath = Path(__file__).parent / "camera/splash.jpg"
simg = ImageTk.PhotoImage(Image.open(spath).resize((W,H)))
my = Label(sroot,image=simg)
my.image = simg
my.pack(fill=BOTH) # .place(x=0,y=0)

Frame(sroot) # ,height=516,width=5).place(x=520,y=0)
lbl1 = Label(sroot,text="Loading ...") # , fg = 'red', bg='#000000'
lbl1.config(anchor=CENTER)
# lbl1.place(x = 300, y = 300)

#MainScreen
def mainroot():    
    import ttkbootstrap as ttk

    if __package__:
        from .camera.ttk import MainApp
    else:
        import sys, os
        sys.path.append(Path(__file__).parent)
        print(Path(__file__).parent)
        from camera.ttk import MainApp

    app = ttk.Window("Raspi Control Panel")
    app.geometry('1024x768')
    app.attributes('-fullscreen', True)
    MainApp(app)

# After this call the main window here
def call_mainroot():
	sroot.destroy()
	mainroot()

sroot.after(2000,call_mainroot)         #TimeOfSplashScreen
mainloop()