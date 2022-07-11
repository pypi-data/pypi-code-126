import browsers
from selenium import webdriver
import os
import logging

logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = '0'
path = r".\\Drivers"

def get_driver():
    if browsers.get('chrome'):
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return webdriver.Chrome(ChromeDriverManager(path=path).install(), options=options)
    if browsers.get('firefox'):
        from webdriver_manager.firefox import GeckoDriverManager
        return webdriver.Firefox(executable_path=GeckoDriverManager(path=path).install())
    if browsers.get('msedge'):
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        return webdriver.Edge(EdgeChromiumDriverManager(path=path).install())
    if browsers.get('opera'):
        from webdriver_manager.opera import OperaDriverManager
        return webdriver.Opera(executable_path=OperaDriverManager(path=path).install())


# driver = get_driver()
