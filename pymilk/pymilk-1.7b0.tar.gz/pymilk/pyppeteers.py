# 移除automation标识符, 避免被识别出来是模拟机
from pyppeteer import launcher
try:
    launcher.DEFAULT_ARGS.remove('--enable-automation')
except:
    pass
# 导入模块
import win32gui
import asyncio
from random import choices
from collections import deque
from json import dumps as json_dumps
from pyppeteer.element_handle import ElementHandle
from pyppeteer.launcher import Launcher
from .pyautogui_repair import screenWidth, screenHeight
from .win32plus import win32plus


headersUa = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

launchArgs = [
    "--start-maximized",  # 窗口默认为最大化
    '--disable-infobars',
    '--no-sandbox',
    f"--user-agent={headersUa}",
]


class _xpathTask():
    def __init__(self, pageT, document, xpath_task):
        self.pageT = pageT
        self.document = document
        self.xpath_task = xpath_task

    def _getitemAssist(self, ele):
        eletyp = type(ele)
        if eletyp is ElementHandle:
            return eleTool(self.pageT, self.document, ele)
        print(f"_getitemAssist发现新的类型: {eletyp}")
        return eleTool(self.pageT, self.document, ele)

    async def _getitem(self, key):
        result = await self.xpath_task
        result = result.__getitem__(key)
        if type(result) is list:
            return [self._getitemAssist(x) for x in result]
        return self._getitemAssist(result)

    def __getitem__(self, key):
        return self._getitem(key)


class _frameTask():
    def __init__(self, pageT, xparam):
        self.pageT = pageT
        self.page = pageT.page
        self.xparam = xparam
    
    async def _getitem(self, key):
        vs = self.xparam['vs']
        kvs = self.xparam['kvs']
        result = [(fr, ele) for fr in self.page.frames for ele in await fr.xpath(*vs, **kvs)]
        result = result[key]
        if type(result) is list:
            return [eleTool(self.pageT, fr, ele) for fr, ele in result]
        return eleTool(self.pageT, result[0], result[1])

    def __getitem__(self, key):
        return self._getitem(key)


class eleTool():
    def __init__(self, pageT, document, ele):
        self.browserT = pageT.browserT
        self.browser = pageT.browser
        self.pageT = pageT
        self.page = pageT.page
        self.document = document
        self.ele = ele

    async def click(self):
        self.browserT.show()
        await asyncio.sleep(0.1)
        await self.page.bringToFront()  # 切换到此标签
        await asyncio.sleep(0.1)
        await self.ele.click()

    async def eval(self, string:str): return await self.document.evaluate(string, self.ele)

    async def innerHTML(self): return await self.eval('ele => ele.innerHTML')  # 子孙元素
    async def outerHTML(self): return await self.eval('ele => ele.outerHTML')  # 子孙元素 + 自身
    async def innerText(self): return await self.eval('ele => ele.innerText')  # 返回浏览器的显示内容
    async def outerText(self): return await self.eval('ele => ele.outerText')  # 读取时同innerText, 写入时覆盖整个元素
    async def textContent(self): return await self.eval('ele => ele.textContent')  # 返回源码的内容, src浏览器不显示, 因此只能用textContent
    async def getAttribute(self, name): return await self.eval(f'ele => ele.getAttribute("{name}")')
    async def hide(self): return await self.eval(f'ele => ele.setAttribute("style", "display: none")')
    
    async def input(self, text, *vs, **kvs):
        await self.ele.type(text, *vs, **kvs)
    
    def xpath(self, *vs, **kvs):
        # await eleT.xpath('......')[:]  # 返回所有结果
        # await eleT.xpath('......')[0]  # 返回第1个结果
        # await eleT.xpath('......')[-1]  # 返回最后1个结果
        return _xpathTask(self.pageT, self.document, self.ele.xpath(*vs, **kvs))
    
    async def getGps(self, key=None):
        gps = await self.eval('''ele => {
            const {width, height, top, left, bottom, right} = ele.getBoundingClientRect()
            return {width, height, top, left, bottom, right}
        }''')
        gps = {
            't': gps['top'],  # 离开可视区顶部的距离
            'r': gps['right'],  # 离开可视区左侧的距离
            'b': gps['bottom'],  # 离开可视区顶部的距离
            'l': gps['left'],  # 离开可视区左侧的距离
            'w': gps['width'],
            'h': gps['height'],
        }
        if key:
            return gps[key]
        return gps


class pageTool():
    def __init__(self, browserT, page):
        self.browserT = browserT
        self.browser = browserT.browser
        self.page = page
        self.goto = page.goto
        self.close = page.close
        self.evaluate = page.evaluate
        self.eval = page.evaluate
        self.content = page.content
        self.show = page.bringToFront
        self.setViewport = page.setViewport

    async def setTitle(self, title):
        await self.eval(f"document.title = {json_dumps(title, ensure_ascii=False)}")

    async def innerHeight(self):
        return await self.eval('''window.innerHeight''')

    async def maximize(self):
        ''' 使页面铺满浏览器可视区 '''
        innerHeight = await self.innerHeight()
        await self.setViewport({'width':screenWidth, 'height':innerHeight})  # 目的: width强制铺满

    def xpath(self, *vs, **kvs):
        # await pageT.xpath('......')[:]  # 返回所有结果
        # await pageT.xpath('......')[0]  # 返回第1个结果
        # await pageT.xpath('......')[-1]  # 返回最后1个结果
        return _xpathTask(self, self.page, self.page.xpath(*vs, **kvs))

    async def waitForXPath(self, *vs, **kvs):
        # await pageT.waitForXPath('......', timeout=30)
        ele = await self.page.waitForXPath(*vs, **kvs)
        return eleTool(self, self.page, ele)

    def frameXpath(self, *vs, **kvs):
        # await pageT.frameXpath('......')[:]  # 返回从所有frame中查找到的所有结果
        # await pageT.frameXpath('......')[0]  # 返回从所有frame中查找到的第1个结果
        # await pageT.frameXpath('......')[-1]  # 返回从所有frame中查找到的最后1个结果
        return _frameTask(self, {'vs':vs, 'kvs':kvs})

    async def scrollToBottom(self):
        ''' 使页面滚动到底部 '''
        html = await self.waitForXPath('html')
        step = max(10, (await self.innerHeight()) // 50)
        aimStep = 0
        tops = deque(maxlen=3)
        while True:
            tops.append(await html.getGps('t'))
            if len(tops) == 3 and len(set(tops)) == 1:
                break
            aimStep += step
            await self.scrollTo(0, aimStep)
            await asyncio.sleep(0.001)

    async def scrollTo(self, x, y):  # (x, y)是要滚动到可视区左上角的文档的坐标
        self.browserT.show()
        await asyncio.sleep(0.1)
        await self.page.bringToFront()  # 切换到此标签
        await asyncio.sleep(0.1)
        await self.eval(f"window.scrollTo({x}, {y})")


class _pagesTask():
    def __init__(self, browserT):
        self.browserT = browserT

    async def _getitem(self, key):
        result = await self.browserT.browser.pages()
        result = result.__getitem__(key)
        if type(result) is list:
            return [pageTool(self.browserT, x) for x in result]
        return pageTool(self.browserT, result)

    def __getitem__(self, key):
            return self._getitem(key)


class browserTool():
    def __init__(self, browser):
        self.browser = browser
        self.close = browser.close
        self.pages = _pagesTask(self)

    async def newPage(self):
        pageT = pageTool(self, await self.browser.newPage())
        await pageT.maximize()
        return pageT

    def setVid(self, vid):
        '''
        vid: 浏览器在win32中的窗口ID
        '''
        self.vid = vid

    def show(self):
        ''' 显示浏览器, 是最小化的逆操作 '''
        win32plus.showView(self.vid)


async def launchTool(options=None, headless=False, **kwargs):
    browserT = browserTool(await Launcher(options, headless=headless, **kwargs).launch())
    pageT = await browserT.pages[0]
    while True:
        num = ''.join(choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=20))
        await pageT.setTitle(num)
        await asyncio.sleep(1)
        lis = []
        func = lambda wid, lis: lis.append(wid)
        win32gui.EnumWindows(func, lis)
        lis = [x for x in lis if num in win32gui.GetWindowText(x)]
        if len(lis) == 1:
            browserT.setVid(lis[0])
            browserT.show()
            return browserT
        await asyncio.sleep(1)
