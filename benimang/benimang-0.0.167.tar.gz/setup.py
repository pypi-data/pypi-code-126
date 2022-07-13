version = "0.0.167"
install_requires = [
    "aiohttp",
    "aiofiles",
    "python-dateutil",
    "twine",         # pip 上传包
    "pyinstaller",
    "openpyxl",
    "pytest",
    "pytest-asyncio",
    "pyecharts",     # 在python 3.10.0版本会报错需要改动 from collections.abc import Iterable
    "chardet",
    "playwright",    # playwright install chromium 需要执行安装浏览器
    "ipython",
    "nest-asyncio",  # ipython报错This event loop is already running；可以使用 nest_asyncio.apply() 解决
    "autopep8",
    "pyperclip",     # copy / paste
    "colorama",      # windows打印带颜色
    "typer",         # fastapi 命令行版本的 fastapi
    "tzdata",        # zoneinfo在windows下需要这个库的支持
    "portalocker",   # 文件锁
    "qrcode",
    "mkdocs",
    "mkdocs-material", 
    "aiosqlite",
    "prettytable",   # 命令行表格
    "tqdm",          # 命令行进度条
    "pretty_errors", # 格式化出错信息
    "aioconsole",    # aioconsole.ainput 可以异步等待输入
    "pyautogui",     # 控制鼠标键盘等（有点像按键精灵）
    # "yappi",       # profile支持asyncio（Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/）
    # "snakeviz",    # 可视化profile查看
]

from setuptools import setup, find_packages

setup(
    name = "benimang",
    version = version,
    keywords="beni",
    description = "utils library for Beni",
    license = "MIT License",
    url = "https://pytask.com",
    author = "Beni",
    author_email = "benimang@126.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = install_requires,
    entry_points={
        "console_scripts": ["beni=beni.cmd:main"],
    },
)