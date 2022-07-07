import psutil
import sys
import stopit
import threading
import os
try:
    import thread
except ImportError:
    import _thread as thread
import datetime
import threading
import json

__version__ = "0.1.0"
__author__ = 'Alawi Hussein Adnan Al Sayegh'
__description__ = 'blocker to block programs until an event happens'
__license__ = """
Copyright 2022 "Alawi Hussein Adnan Al Sayegh"
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
and the names are copyrighted
"""
name = "ProTimer"

done = False
fndata = "data.time"
fnlogs = "logs.time"
class date(object):
	"""date object"""
	def __init__(self, day, hour, minute, second):
		super(date, self).__init__()
		self.__dict__.update(dict(day=day, hour=hour, minute=minute, second=second))
	def __tuple__(self):
		return (self.day, self.hour, self.minute, self.second)
	@property
	def tuple(self):
		return self.__tuple__()
	def __str__(self):
		return f"{self.day}:{self.hour}:{self.minute}:{self.second}"
	def __repr__(self):
		return f"(day={self.day}, hour={self.hour}, minute={self.minute}, second={self.second})"
def maketime(time):
	day = time // (24 * 3600)
	time = time % (24 * 3600)
	hour = time // 3600
	time %= 3600
	minutes = time // 60
	time %= 60
	seconds = time
	return date(day, hour, minutes, seconds)
def threader(timer,fn=fndata): # timer at sec
	def write(obj):
		try:
			with open (fn,"w") as f:
				 f.write(str(obj))
		except FileNotFoundError as e:
			with open (fn,"a") as f:
				 f.write(str(obj))
	ddn = datetime.datetime.now()
	time = maketime((timer+ddn.second)+(ddn.minute*60)+((ddn.hour*60)*60))
	write(json.dumps(time.__dict__))
class timer(object):
	def __init__(self,sec,fn=fndata):
		super(timer, self).__init__()
		self.Thread = threading.Thread(target=threader, args=[sec,fn])
	def start(self):
		global done
		done = False
		return self.Thread.start()
	def close(self):
		global done
		done = True
class TimeOutProcess(Exception):
	""" when run_until_completed in timeout """
	def __init__(self, message,args,timeout=None):
		super(TimeOutProcess, self).__init__()
		self.args = args
		self.message = message
	def __str__(self):
		if len(self.args) < 0:
			return self.message
		def formated(string,replaceit,tesk):
			return string.replace(replaceit,tesk)
		message = self.message
		for i in range(len(self.args)):
			message = formated(message,"{"+str(i)+"}",str(self.args[i]))
		return message
	def __repr__(self):
		return f"{self.__class__.__name__}({repr(str(self))})"



class _object_(object):
	"""save data any(kws/args)"""
	def __init__(self,*args, **kw):
		super(_object_, self).__init__()
		self.__dict__ = kw
		self.__args__ = args
class system(object):
	def read(fn=fndata):
		try:
			with open (fn,"r") as f:
				return f.read()
		except FileNotFoundError as e:
			return "{\"hour\":0,\"minute\":0,\"second\":0}"
	def write(obj,fn=fnlogs):
		with open (fn,"a") as f:
			 f.write(str(obj))
	def sleep():
		while True:
			try:
				r = _object_(**json.loads(system.read()))
				hms = r.hour,r.minute,r.second
				date = datetime.datetime.now()
				if (date.hour,date.minute,date.second) == hms:
					break
			except json.decoder.JSONDecodeError as e:
				system.write(e.__class__.__name__+": "+str(e)+"\n",fn=fnlogs)
	def get_procs():
		programs = {}
		# Iterate over all running process
		errors = []
		for proc in psutil.process_iter():
			try:
				# Get process name & pid from process object.
				processName = proc.name()
				processID = proc.pid
				if processName not in programs:
					InfoDict = proc.as_dict(attrs=['pid', 'name'])
					programs[processName] = {}
					programs[processName]["pids"] = [processID]
				else:
					programs[processName]["pids"].append(processID)
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as error:
				errors.append((proc,error))
		return programs, errors
	def is_running(name,pids,call=None,callback=True):
		"""
		if a process is running or not
		return a booling
		if is running return True
		else is not running return False
		"""
		if call is None:
			call = system.get_procs
		if callable(call) and callback:
			dict,errors = call()
		else:
			dict = call
		if name in dict:
			try:
				if not listsin(pids,programs[name]["pids"]):
					return False
				else:
					return True
			except Exception:
				pass
		else:
			return False
		return True
	def run_until(name,pids=None):
		"""
		wait until the process is finish
		return only True
		"""
		while True:
			if not system.is_running(name,pids):
				return True
			else:
				pass
		return False
	def run_until_completed(name,pids=None,timeout=10,default=True,**kw):
		"""
		some as run_until but with a timeout
		return tuple => (TimeOutProcess(),False) if timeout else (returns_function,True)
		"""
		timeout_param = kw.get("timeout_param", "return_timeout")
		default = kw.get("default",TimeOutProcess("TimeOut: timeout '{1}'",(pids,name),timeout=timeout))
		kw["default"] = default
		kw["timeout_param"] = timeout_param
		@stopit.threading_timeoutable(**kw)
		def run(name,pids=pids):
			return (system.run_until(name,pids))
		result = run(name,pids=pids , return_timeout=timeout)
		if result is True:
			return result, False
		else:
			return result, True

def listsin(listA,listB):
	for itemB in listB:
		if itemB in listA:
			return True
	return False

class timerquit(object):
	"""
	if the function took too long it raise KeyboardInterrupt
	@timerquit.exit_after(9)
	def foo(bar):
	    print ('hello {0}'.format(bar))
	    time.sleep(10)
	    return ("foo")
	try:
		print(foo(bar="hello"))
	except KeyboardInterrupt:
		pass
	"""
	def quit_function(fn_name,show):
		"""
		raise KeyboardInterrupt to thread
		"""
		# print to stderr, unbuffered in Python 2.
		if show:
			print('{0} took too long'.format(fn_name), file=sys.stderr)
			sys.stderr.flush() # Python 3 stderr is likely buffered.
		thread.interrupt_main() # raises KeyboardInterrupt

	def exit_after(s,show=True):
		'''
		use as decorator to exit process if 
		function takes longer than s seconds
		'''
		def outer(fn):
			def inner(*args, **kwargs):
				timer = threading.Timer(s, timerquit.quit_function, args=[fn.__name__,show])
				timer.start()
				try:
				    result = fn(*args, **kwargs)
				finally:
				    timer.cancel()
				return result
			return inner
		return outer



"""
HOW TO MAKE SYSTEM.SLEEP(seconds):
	FIRST SAVE THE DATE IN A FILE TO CHECK IT
	THE TWO PROGRAMS START AT WHAT
	THEN READ FILE AND IF THE DATE IS DATE
	THEN STOP BLOCKING THE PRGRAM
THE END SLEEP(X);
"""


