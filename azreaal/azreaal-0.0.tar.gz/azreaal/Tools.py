import os
import time
import platform
from .Tools import OSTools as ost
from .Tools import XLSXTools as xst
from selenium import webdriver
from selenium.webdriver.common.by import By


class OSTools:
    def RefreshTerminal(header):
        time.sleep(0.01)
        os.system("cls" if platform.system() == "Windows" else "clear")
        time.sleep(0.01)
        print(header)

    def FileSlash():
        return "/" if platform.system() != "Windows" else "\\"

    def WaitOnDownload(filNam, loc):
        downloadPath = os.getcwd()
        downloadPath += ost.FileSlash() + loc + ost.FileSlash()
        filename = ""
        end = False
        while not end:
            with os.scandir(downloadPath) as entries:
                for entry in entries:
                    if entry.is_file():
                        try:
                            nams = entry.name.split(".")
                            if len(nams) == 2 and nams[1] == "xlsx":
                                if nams[0][0:9] == filNam:
                                    filename = downloadPath + entry.name
                                    end = True
                        except:
                            print(
                                "Whoops! Hit a snag processing that. Let me get us back on track, one second..."
                            )
                            time.sleep(2)
            time.sleep(1)
        return filename

    def FindDownload(filNam, loc):
        downloadPath = os.getcwd()
        downloadPath += ost.FileSlash() + loc + ost.FileSlash()
        filename = ""
        end = False
        while not end:
            with os.scandir(downloadPath) as entries:
                for entry in entries:
                    if entry.is_file():
                        try:
                            nams = entry.name.split(".")
                            if len(nams) == 2 and nams[1] == "xlsx":
                                if nams[0][0:9] == filNam:
                                    filename = downloadPath + entry.name
                                    end = True
                                else:
                                    print(
                                        "We found a file, but it's wrong!\n"
                                        + nams[0][0:9]
                                        + " and "
                                        + filNam
                                    )
                        except:
                            print("Can't find that file!")
        return filename

    def SetNameWidth(itName, width):
        SCREENWIDTH = width
        name = itName
        if len(itName) > SCREENWIDTH:
            name = itName[0 : (SCREENWIDTH - 1)]
        else:
            name = itName
            while len(name) < SCREENWIDTH:
                name += " "
        return name


class SeleniumTools:
    name = "tool"

    def GetNewWebdriver(loc, vis):
        option = webdriver.ChromeOptions()
        downloadPath = os.getcwd()
        prefs = {
            "profile.default_content_setting_values.automatic_downloads": 1,
            "download.default_directory": downloadPath
            + (ost.FileSlash() + loc + ost.FileSlash()),
        }
        if not vis:
            option.add_argument("--no-sandbox")
            option.add_argument("--headless")
            option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--log-level=OFF")
        option.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(
            options=option,
            service_log_path=os.devnull,
        )
        return driver

    def GetElementByID(driver, log, id):
        try:
            return driver.find_element(By.ID, id)
        except:
            print("Couldn't find id for " + log)
        try:
            return driver.find_element(By.ID, id)
        except:
            print("Couldn't find id for " + log)

    def GetElement(driver, log, xpath, css):
        try:
            return driver.find_element(By.XPATH, xpath)
        except:
            print("Couldn't find xpath for " + log)
        try:
            return driver.find_element(By.CSS_SELECTOR, css)
        except:
            print("Couldn't find css for " + log)
        try:
            return driver.find_element(By.XPATH, xpath)
        except:
            print("Couldn't find xpath for " + log)
        try:
            return driver.find_element(By.CSS_SELECTOR, css)
        except:
            print("Couldn't find css for " + log)


class XLSXTools:
    def CharAdd(char, addition):
        full_char = ""
        if len(char) > 1 and char[len(char) - 1] == "Z":
            # recursively change the last letter from Z to A, and add 1 to the preceeding one
            full_char = xst.CharAdd(char[0 : len(char - 1)], 1)
        elif len(char) > 1:
            full_char = char[0 : len(char - 1)]
            char = char[len(char) - 1]
        elif char == "Z":
            full_char = "A" + full_char + "A"
            return full_char
        else:
            return full_char + str(chr(ord(char) + int(addition)))

    def GetColumn(sheet, column_label):
        end = False
        sheetchr = "A"
        while not end:
            label = sheet[sheetchr + "1"].value
            if label == column_label:
                return sheetchr
            else:
                sheetchr = CharAdd(sheetchr, 1)
                if sheetchr == "AD":
                    input("Got to AD!")
