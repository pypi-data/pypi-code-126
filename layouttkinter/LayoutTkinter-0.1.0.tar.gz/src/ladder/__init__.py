"""自动化提交到github并且执行pyinstaller进行构建
"""
from tkinter import *
from typing import List, Tuple, Iterable
from widgets import Btn, Lab, BaseWidget, Cbox, Input, RadioGroup, ChooseFile


class Window(Tk):
    def __init__(self, title: str, layout: List):
        super().__init__()
        self.title(title)
        self.center((600, 460))
        self.layout = layout
        self._build_layout()
        self._active = True
        self.wm_protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self._active = False
        self.quit()

    def center(self, size: Tuple[int, int] = None):
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = int((w - size[0]) / 2), int((h - size[1]) / 2)
        self.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

    def _build_layout(self):
        for index, row in enumerate(self.layout):
            if isinstance(row, Iterable):
                for column, widget in enumerate(row):
                    if isinstance(widget, BaseWidget):
                        widget(self, row=index, column=column, padx=5, pady=5, sticky=NSEW)

    def mainloop(self, n: int = 0) -> bool:
        """窗口事件循环
        :param n: n < 0 主循环永远阻塞  n == 0 主循环不阻塞  n > 0主循环超时退出(毫秒)
        :return: 窗口是否关闭
        """
        if n == 0:
            self.update()
        else:
            if n > 0:
                self.after(n, self.quit)
            super().mainloop()
        return self._active


if __name__ == '__main__':
    app = Window("app", layout=[
        [Btn(text="apple"), Btn(text="Orange")],
        [Lab(text="bbq")],
        [Cbox(text="单文件"), Cbox(text="无窗口")],
        [Input(text="输入啥呢")],
        [RadioGroup(["a", "b", "c"])],
        [ChooseFile("选择执行脚本", suffix=".py")]
    ])
    app.mainloop(-1)
