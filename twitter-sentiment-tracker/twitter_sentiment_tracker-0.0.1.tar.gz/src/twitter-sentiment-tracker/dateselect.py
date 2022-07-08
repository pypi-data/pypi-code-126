import tkinter as tk
from tkcalendar import *
from tkinter import ttk
import datetime as dt
import math

class TwitterAPIArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class Cal_Impl:

    def __init__(self, enabled):
        #set up tkinter objects for initial display
        self.ws = tk.Tk()
        
        cal_label_frame = tk.Frame(self.ws)
        fzero = tk.Frame(self.ws)
        fone = tk.Frame(fzero)
        ftwo = tk.Frame(fzero)
        
        self.start_cal_label = tk.Label(
            cal_label_frame, 
            text="Select Start Date For Tweet Collection",
            font=("Times", 12),
            bg="#cae7e8"
            )
        self.end_cal_label = tk.Label(
            cal_label_frame, 
            text="Select End Date For Tweet Collection",
            font=("Times", 12),
            bg="#cae7e8"
            )
            
        fone.pack(side=tk.LEFT, padx=10, pady=10)
        ftwo.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.start_cal_label.pack(side=tk.LEFT, padx=10, pady=(2,5))
        self.end_cal_label.pack(side=tk.RIGHT, padx=10, pady=(2,5))
        
        cal_label_frame.pack(side=tk.TOP)
        cal_label_frame.config(bg="#cae7e8")
        
        fzero.pack(side=tk.TOP)
        fzero.config(bg="#cae7e8")
        
        #calculate maximum and minimum days that can be queried on Twitter Search API
        delta_day = dt.timedelta(days = 1)
        tw_start_date = dt.date(2006,3,21)
        
        self.start_cal = Calendar(
            fone, 
            selectmode="day", 
            mindate = tw_start_date,
            maxdate = dt.datetime.now() - delta_day,
            side=tk.LEFT
            )
        
        self.end_cal = Calendar(
            ftwo, 
            selectmode="day", 
            mindate = tw_start_date,
            maxdate = dt.datetime.now(),
            side=tk.RIGHT
            )
            
        self.msg = tk.Label(
            self.ws, 
            text="How long should data collection intervals be?",
            font=("Times", 12),
            bg="#cae7e8"
            )
        self.msg2 = tk.Label(
            self.ws, 
            text="How many tweets should be collected per interval?",
            font=("Times", 12),
            bg="#cae7e8"
            )
        self.msg_display = tk.Label(
            self.ws,
            text="",
            bg="#cae7e8"
        )
        
        #initialize combobox for interval length variable selection
        self.interval_bxstr = tk.StringVar(value = 240)
        self.interval_bx = ttk.Combobox(self.ws, textvariable=self.interval_bxstr)
        #self.interval_bx.bind('<<ComboboxSelected>>', interval_chosen)
        self.interval_bx['values'] = (60,240,1440)
        self.interval_bx.config(width = 15)
        
        #if default data collection is selected
        if not enabled:
            self.interval_bx.config(state=tk.DISABLED)
            
        #initialize combobox for interval length variable selection
        self.max_bxstr = tk.StringVar(value = 10)
        self.max_bx = ttk.Combobox(self.ws, textvariable=self.max_bxstr)
        #self.interval_bx.bind('<<ComboboxSelected>>', interval_chosen)
        self.max_bx['values'] = (10,50,100,1000)
        self.max_bx.config(width = 15)
        
        #if default data collection is selected
        if not enabled:
            self.max_bx.config(state=tk.DISABLED)
            
        #declare and initialize variables used to send data outside of the class
        self.end_dt = dt.datetime.now(dt.timezone.utc)
        self._totaltime = 0
        self._datestr2 = ""
        self._interval_len = 0
        self._datestr = ""
        self._json_max = 0
        self._has_values = False
        
    def on_quit(self):
        print("Calendar was terminated by exiting the window")
        self.ws.destroy()
        
    def display_msg(self):
        #retrieve selected start and end date from calendar  
        self._datestr = self.start_cal.get_date()
        
        self._datestr2 = self.end_cal.get_date()

        date_r = self._datestr.split("/")
        date2_r = self._datestr2.split("/")
        
        #adding the 2000 is bad practice, but this code will not exist in the year 3000 and twitter did not exist in 1999
        date = dt.date(int(date_r[2])+2000, int(date_r[0]), int(date_r[1]))
        date2 = dt.date(int(date2_r[2])+2000, int(date2_r[0]), int(date2_r[1]))
        
        #retrieve timezone-aware time at exactly midnight UTC
        ti = dt.time(tzinfo = dt.timezone.utc)
        
        self.start_dt = dt.datetime.combine(date,ti)
        self.end_dt = dt.datetime.combine(date2,ti)
        
        #retrieve use selections from comboboxes
        self._interval_len = self.interval_bx.get()
        self._json_max = self.max_bx.get()
        
        self._totaltime = (self.end_dt-self.start_dt)/dt.timedelta(minutes = 1)
        
        t = f"Your query is for tweets created between {self._datestr} and {self._datestr2} with data collection intervals of length {self._interval_len} minutes."
        print(t)
        
        #check for illegal arguments 
        if float(self._interval_len) < 1:
            raise TwitterAPIArgumentError(f"Invalid time interval ({self._interval_len}) received")
        pluralizer = "s" if float(self._interval_len) > 1 else ""
        if float(self._json_max) < 1:
            raise TwitterAPIArgumentError(f"Invalid rate of tweets ({self._json_max}) per ({self._interval_len}) minute{pluralizer} requested. At least one tweet must be requested per time interval.") 
        
        self._has_values = True
        #once user selects search parameters, UI is no longer necesssary
        self.ws.quit()
    
    #getter methods for user input
    @property   
    def interval_len(self):
        return self._interval_len
    @property
    def totaltime(self):
        return self._totaltime
    @property
    def datestr(self):
        return self._datestr
    @property
    def datestr2(self):
        return self._datestr2
    @property
    def json_max(self):
        return self._json_max
    @property
    def has_values(self):
        return self._has_values
        
    def run_cal(self):
        self.ws.title("Set Date Range for Data Collection")
        self.ws.geometry("600x430")
        self.ws.config(bg="#cae7e8")#819394 #cae7e8 borderwidth
        self.ws.config(borderwidth=15)
        
        self.start_cal.pack()
        self.end_cal.pack()

        actionBtn = tk.Button(
            self.ws,
            text="Run Query",
            command=self.display_msg
        )
        
        self.interval_bx.pack(side=tk.BOTTOM, expand=False, pady=2)
        self.msg.pack(side=tk.BOTTOM, pady=2)
        
        self.max_bx.pack(side=tk.BOTTOM, expand=False, pady=2)
        self.msg2.pack(side=tk.BOTTOM, pady=2)
        actionBtn.pack(side=tk.BOTTOM, pady=2)
        
        self.msg_display.pack(side=tk.BOTTOM, pady=3)
        
        self.ws.protocol('WM_DELETE_WINDOW', self.on_quit)
        self.ws.mainloop()
        
class Cal_End:

    def __init__(self, enabled):
        #set up tkinter objects for initial display
        self.ws = tk.Tk()
        
        #calculate maximum and minimum days that can be queried on Twitter Search API
        delta_day = dt.timedelta(days = 1)
        tw_start_date = dt.date(2006,3,21)

        self.end_cal = Calendar(
            self.ws, 
            selectmode="day", 
            mindate = tw_start_date,
            maxdate = dt.datetime.now()
            )
        self.msg = tk.Label(
            self.ws, 
            text="How long should data collection intervals be?",
            font=("Times", 12),
            bg="#cae7e8"
            )
        self.msg2 = tk.Label(
            self.ws, 
            text="How many tweets should be collected per interval?",
            font=("Times", 12),
            bg="#cae7e8"
            )
        self.msg_display = tk.Label(
            self.ws,
            text="",
            bg="#cae7e8"
        )
        
        #initialize combobox for interval length variable selection
        self.interval_bxstr = tk.StringVar(value = 240)
        self.interval_bx = ttk.Combobox(self.ws, textvariable=self.interval_bxstr)
        #self.interval_bx.bind('<<ComboboxSelected>>', interval_chosen)
        self.interval_bx['values'] = (60,240,1440)
        self.interval_bx.config(width = 15)
        
        #if default data collection is selected, parameter selection is unnecessary
        if not enabled:
            self.interval_bx.config(state=tk.DISABLED)
            
        #initialize combobox for interval length variable selection
        self.max_bxstr = tk.StringVar(value = 10)
        self.max_bx = ttk.Combobox(self.ws, textvariable=self.max_bxstr)
        #self.interval_bx.bind('<<ComboboxSelected>>', interval_chosen)
        self.max_bx['values'] = (10,50,100,1000)
        self.max_bx.config(width = 15)
        
        #if default data collection is selected, parameter selection is unnecessary
        if not enabled:
            self.max_bx.config(state=tk.DISABLED)
            
        #declare and initialize variables used to send data outside of the class
        self.end_dt = dt.datetime.now(dt.timezone.utc)
        self._datestr2 = ""
        self._interval_len = 0
        self._datestr = ""
        self._json_max = 0
        self._has_values = False
    def on_quit(self):
        print("Calendar was terminated by exiting the window")
        self.ws.destroy()
        
    def display_msg(self):
        #retrieve selected end date from calendar         
        self._datestr2 = self.end_cal.get_date()

        date2_r = self._datestr2.split("/")
        
        #adding the 2000 is bad practice, but this code will not exist in the year 3000 and twitter did not exist in 1999
        date2 = dt.date(int(date2_r[2])+2000, int(date2_r[0]), int(date2_r[1]))
        
        #retrieve timezone-aware time at exactly midnight UTC
        ti = dt.time(tzinfo = dt.timezone.utc)
        
        self.end_dt = dt.datetime.combine(date2,ti)
        
        #retrieve use selections from comboboxes
        self._interval_len = self.interval_bx.get()
        self._json_max = self.max_bx.get()

        
        t = f"Your query is for tweets created before {self._datestr2} with data collection intervals of length {self._interval_len} minutes."
        print(t)
 
        #check for illegal arguments 
        if float(self._interval_len) < 1:
            raise TwitterAPIArgumentError(f"Invalid time interval ({self._interval_len}) received")
        pluralizer = "s" if float(self._interval_len) > 1 else ""
        if float(self._json_max) < 1:
            raise TwitterAPIArgumentError(f"Invalid rate of tweets ({self._json_max}) per ({self._interval_len}) minute{pluralizer} requested. At least one tweet must be requested per time interval.")  

        self._has_values = True
        
        #once user selects search parameters, UI is no longer necesssary
        self.ws.quit()
    
    #getter methods for user input
    @property   
    def interval_len(self):
        return self._interval_len
    @property
    def datestr2(self):
        return self._datestr2
    @property
    def json_max(self):
        return self._json_max
    @property
    def has_values(self):
        return self._has_values
        
    def run_cal(self):
        self.ws.title("Set Date Range for Data Collection")
        self.ws.geometry("600x430")
        self.ws.config(bg="#cae7e8")
        self.ws.config(borderwidth=15)
        
        self.end_cal_label = tk.Label(
            self.ws, 
            text="Select End Date For Tweet Collection",
            font=("Times", 12),
            bg="#cae7e8"
            )
            
        self.end_cal_label.pack(side = tk.TOP, pady = 5)
        self.end_cal.pack(side = tk.TOP)

        actionBtn = tk.Button(
            self.ws,
            text="Run Query",
            padx=10,
            pady=10,
            command=self.display_msg
        )
        self.interval_bx.pack(side=tk.BOTTOM, expand=False, pady=2)
        self.msg.pack(side=tk.BOTTOM, pady=2)
        
        self.max_bx.pack(side=tk.BOTTOM, expand=False, pady=2)
        self.msg2.pack(side=tk.BOTTOM, pady=2)
        actionBtn.pack(side=tk.BOTTOM, pady=2)
        
        self.msg_display.pack(side=tk.BOTTOM, pady=3)
        
        self.ws.protocol('WM_DELETE_WINDOW', self.on_quit)
        self.ws.mainloop()
