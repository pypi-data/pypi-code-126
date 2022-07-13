from tkinter import StringVar, LEFT, BOTH, YES
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from collections import ChainMap
from typing import Union, Tuple, Optional


class BaseWidget:
    def __init__(self, text: str = None, **kwargs):
        self.kwargs = kwargs
        if text is not None:
            self.kwargs["text"] = text

    def __call__(self, master, **kwargs):
        ...


class Btn(BaseWidget):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def __call__(self, master, **kwargs):
        self.widget = Button(master, **self.kwargs)
        self.widget.grid(**kwargs)
        return self


class Lab(BaseWidget):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def __call__(self, master, **kwargs):
        self.text = StringVar()
        self.text.set(self.kwargs.get("text", ""))
        self.kwargs["textvariable"] = self.text
        self.widget = Label(master, **self.kwargs)
        self.widget.grid(**kwargs)
        return self


class Cbox(BaseWidget):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def __call__(self, master, **kwargs):
        self.text = StringVar()
        self.widget = Checkbutton(master, variable=self.text, **self.kwargs)
        self.widget.grid(**kwargs)
        return self


class RadioGroup(BaseWidget):
    def __init__(self, values, **kwargs):
        super().__init__(**kwargs)
        self.values = values

    def __call__(self, master, **kwargs):
        self.text = StringVar()
        self.widget = Frame(master, **self.kwargs)
        self.text.set(self.values[0])
        for value in self.values:
            Radiobutton(self.widget, text=value, value=value, variable=self.text).pack(side=LEFT, fill=BOTH, expand=YES)
        self.widget.grid(**kwargs)
        return self


class Input(BaseWidget):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def __call__(self, master, **kwargs):
        self.text = StringVar()
        self.text.set(self.kwargs.get("text", ""))
        self.kwargs["textvariable"] = self.text
        self.widget = Entry(master, **self.kwargs)
        self.widget.grid(**kwargs)
        return self


class ChooseFile(BaseWidget):
    def __init__(self, title, suffix: Union[str, Tuple], default: Optional[str] = None, parent_dir: str = ".", **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.default = default
        if isinstance(suffix, str):
            suffix = (suffix, )
        self.suffix = suffix
        self.parent = parent_dir

    def __call__(self, master, **kwargs):
        self.widget = Frame(master)
        self.text = Input(self.default or "")(self.widget, row=0, column=0).text
        Btn(self.title, command=self.choose_file)(self.widget, row=0, column=1)
        self.widget.grid(**kwargs)
        return self.widget

    def choose_file(self):
        suffix = [(v.removeprefix(".") + " file", v) for v in self.suffix]
        filename = askopenfilename(
            title=self.title,
            defaultextension=self.suffix[0],
            filetypes=suffix,
            initialdir=self.parent
        )
        if filename:
            self.text.set(filename)
