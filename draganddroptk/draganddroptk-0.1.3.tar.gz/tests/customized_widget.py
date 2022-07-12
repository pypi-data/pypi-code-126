from PIL import Image, ImageTk

from tkinter import Label, Tk
from tkinter.ttk import Separator

from DragAndDropTk import DragAndDropTk

class Improved_DragAndDropTk(DragAndDropTk):
    
    def __init__(self, text: str, img_path: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, borderwidth=3)
                
        self.lbl = Label(self, text=text, bg="#002255", foreground='#ffee77', padx=10, pady=10)
        self.lbl.pack(fill='x')
        
        self.sep = Separator(self, orient='horizontal', style="TSeparator")
        self.sep.pack()
        
        logo = ImageTk.PhotoImage(
            Image.open(img_path)
            .resize((100, 100))
        )

        self.lbl.config
        self.img = Label(self, image=logo, bg="#002255", width=self.lbl.winfo_reqwidth())
        self.img.image = logo
        self.img.pack()
        
        self.bind_child(self.lbl)
        self.bind_child(self.sep)
        self.bind_child(self.img)
        

class MainWindow(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title("Teste Drag and Drop Widget")
        self.geometry(f"1280x720")
        
        self.dnd_widget = Improved_DragAndDropTk(
            text="It's a DragAndDrop with a label and a image", 
            img_path=f"./tests/resources/python-logo.png",
            master=self, width=100, height=50
        )
        self.dnd_widget.pack()
        
        
MainWindow().mainloop()