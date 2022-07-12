from tkinter import Frame


class DragAndDropTk(Frame):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.org_x = self.winfo_x()
        self.org_y = self.winfo_y()
        
        self.bind("<Button-1>", self.drag_start)
        self.bind("<B1-Motion>", self.drag_move)
        self.bind("<B1-ButtonRelease>", self.drag_stop)
        
    def drag_start(self, event) -> None:
        self.start_x = event.x
        self.start_y = event.y
    
    def drag_move(self, event) -> None:
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        
        lim_x = self.master.winfo_width() -  self.winfo_width()
        lim_y = self.master.winfo_height() - self.winfo_height()
        
        if 0 <= x < lim_x and 0 <= y < lim_y:
            self.place(x=x, y=y)
    
    def drag_stop(self, event) -> None:
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
    
        lim_x = self.master.winfo_width() - self.winfo_width()
        lim_y = self.master.winfo_height() -self.winfo_height()
        
        if 0 <= x < lim_x and 0 <= y < lim_y:
            self.org_x = self.winfo_x()
            self.org_y = self.winfo_y()
            
        self.mouse_release_action(self.org_x, self.org_y)
    
    def mouse_release_action(self, pos_x: int, pos_y: int) -> None:
        self.place(x=pos_x, y=pos_y)
        
    def bind_child(self, child) -> None:
        child.bind("<Button-1>", self.drag_start)
        child.bind("<B1-Motion>", self.drag_move)
        child.bind("<B1-ButtonRelease>", self.drag_stop)
        