from PIL import Image, ImageTk

from tkinter import Frame, Label, Tk
from tkinter.ttk import Separator

from DragAndDropTk.drag_and_drop_tk import DragAndDropTk


class Improved_DragAndDropTk(DragAndDropTk):
    
    def __init__(self, text, *args, **kwargs) -> None:
        self.frames = kwargs.pop('frames')
        super().__init__(*args, **kwargs, borderwidth=3)
      
        self.lbl = Label(self, text=text,
                         bg="#002255", foreground='#ffee77', padx=10, pady=10)
        self.lbl.pack(fill='x')
        
        self.sep = Separator(self, orient='horizontal', style="TSeparator")
        self.sep.pack()
        
        logo = ImageTk.PhotoImage(
            Image.open(f"./tests/resources/python-logo.png")
            .resize((100, 100))
        )

        self.lbl.config
        self.img = Label(self, image=logo, bg="#002255", width=self.lbl.winfo_reqwidth())
        self.img.image = logo
        self.img.pack()
                
        self.bind_child(self.lbl)
        self.bind_child(self.sep)
        self.bind_child(self.img)
        
    def mouse_release_action(self, pos_x: int, pos_y: int) -> None:
        for frame in self.frames:
            l = frame.winfo_x()
            t = frame.winfo_y()
            r = frame.winfo_x() + frame.winfo_width()
            b = frame.winfo_y() + frame.winfo_height()
            
            c_x = (l + r) // 2
            c_y = (b + t) // 2            
            
            if l <= pos_x + self.winfo_width()//2 <= r and t <= pos_y + self.winfo_height()//2 <= b:
                self.place(
                    x=c_x - self.winfo_width() // 2,
                    y=c_y - self.winfo_height() // 2
                )
        

class MainWindow(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title("Teste Drag and Drop Widget")
        self.geometry(f"1280x720")
        
        self.main_frame = Frame(self)
        
        self.frm1 = Frame(self.main_frame, bg="#008899")
        self.frm2 = Frame(self.main_frame, bg="#ffee77")
        
        self.frm1.pack(fill='both', expand=1, side='left')
        self.frm2.pack(fill='both', expand=1, side='left')
        
        self.main_frame.pack(fill='both', expand=2)
        
        Improved_DragAndDropTk(
            "I can be dropped inside the frames", master=self,
            frames=[self.frm1, self.frm2] 
        ).place(x=0, y=0)
        
        
        
MainWindow().mainloop()