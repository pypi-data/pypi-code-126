import asyncio
import win32gui, win32con, win32api
from win32clipboard import OpenClipboard, SetClipboardData, CloseClipboard
from .pyautogui_repair import pyautogui


class win32plus():
    vidGetText = win32gui.GetWindowText
    getGps = win32gui.GetWindowRect
    
    def __init__(self):
        pass

    @staticmethod
    def repairShowViewBug():
        # 修复窗口无法置顶
        win32api.SetCursorPos([-1, -1])  # 移动鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左击

    @staticmethod
    def showView(vid):
        ''' 显示指定的窗口 '''
        try:
            win32gui.SetForegroundWindow(vid)
        except:
            win32plus.repairShowViewBug()
            win32gui.SetForegroundWindow(vid)
    
    @staticmethod
    def getVids(fatherVID=None):
        '''
        fatherVID为None时, 查找搜索顶层窗口
        fatherVID非None时, 查找fatherVID的子窗口
        '''
        if fatherVID is None:
            vidList = []
            def winHandle(vid, vidList):
                vidList.append(vid)
            win32gui.EnumWindows(winHandle, vidList)
            return vidList
        else:
            sons = []
            win32gui.EnumChildWindows(fatherVID, lambda hwnd, param: param.append(hwnd),  sons)
            return sons
    
    @staticmethod
    def getVidTree(fatherVID=None):
        '''
        把所有的窗口全部找出来, 根据父-子关系组成树状的dict结构
        '''
        sons = win32plus.getVids(fatherVID)
        return {(x, win32plus.vidGetText(x)):win32plus.getVidTree(x) for x in sons}
    
    @staticmethod
    async def findVid(name, sleep=1):
        ''' 根据窗口的名称查找窗口 '''
        while True:
            vids = [x for x in win32plus.getVids() if win32plus.vidGetText(x) == name]
            if len(vids) == 1:
                return vids[0]
            print(f"找到名称为'{name}'的窗口共{len(vids)}个")
            await asyncio.sleep(sleep)
    
    @staticmethod
    def vidGetCenterGps(vid):
        ''' 提取窗口中心的坐标 '''
        left, top, right, bottom = win32plus.getGps(vid)
        x = (left + right) // 2
        y = (top + bottom) // 2
        return x, y
    
    @staticmethod
    async def clickLeft(x=None, y=None, vid=None, moveDelay=0, clickDelay=0):
        '''
            左击鼠标
        指定x和y时, 左击指定的坐标, 未指定x和y时, 左击当前鼠标在屏幕上的位置
        vid: 指定vid时, 先显示该窗口, 然后再左击鼠标
        moveDelay: 在移动鼠标到指定的(x,y)坐标前, 先延迟该秒数
        clickDelay: 在左击鼠标前, 先延迟该秒数
        '''
        if vid is not None:
            win32plus.showView(vid)
        if None not in (x, y):
            if moveDelay:
                await asyncio.sleep(moveDelay)
            win32api.SetCursorPos([x, y])  # 移动鼠标
        if clickDelay:
            await asyncio.sleep(clickDelay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左击

    @staticmethod
    async def clickRight(x=None, y=None, vid=None, moveDelay=0, clickDelay=0):
        '''
            右击鼠标
        指定x和y时, 右击指定的坐标, 未指定x和y时, 右击当前鼠标在屏幕上的位置
        vid: 指定vid时, 先显示该窗口, 然后再右击鼠标
        moveDelay: 在移动鼠标到指定的(x,y)坐标前, 先延迟该秒数
        clickDelay: 在右击鼠标前, 先延迟该秒数
        '''
        if vid is not None:
            win32plus.showView(vid)
        if None not in (x, y):
            if moveDelay:
                await asyncio.sleep(moveDelay)
            win32api.SetCursorPos([x, y])  # 移动鼠标
        if clickDelay:
            await asyncio.sleep(clickDelay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # 右击

    @staticmethod
    def setClipboard(text):
        ''' 复制字符串到剪贴板 '''
        OpenClipboard()
        SetClipboardData(win32con.CF_UNICODETEXT , text)
        CloseClipboard()

    @staticmethod
    def copyAndPaste(text):
        ''' 复制字符串到剪贴板, 并粘贴 '''
        win32plus.setClipboard(text)
        pyautogui.hotkey('ctrl', 'v', interval=0.1)
