from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as cm
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

__author__ = "Sanjay Kumar Y R"


class Page:
    global driver

    def __init__(self,url):
        try:
            driver.get(url)
        
        except InvalidArgumentException:
            print("Please check the url")


    def get_fields(self,field):
        fields = driver.find_elements(By.TAG_NAME,field)
        out = {}
        keys = ["aria-label","name","placeholder","id","a"]
        for field_element in fields:
            key_out = field_element.text
            if key_out!="" and not key_out.isspace():
                out[key_out] = field_element
                
            for key in keys:
                key_out = field_element.get_attribute(key)
                if key_out!=None and key_out!="":
                    out[key_out] = field_element
                    
        return out

    def click_button_using_clue(self,clue):
        self.get_buttons()[clue].click()

    def submit_on_element_using_clue(self,clue,text):
        ele = self.get_inputs()[clue]
        self.submit(ele,text)


    def write_on_element_using_clue(self,clue,text):
        ele = self.get_inputs()[clue]
        self.write(ele,text)

    def go_to(self,clue):
        self.get_links()[clue].click()

    def get_all(self):
        self.fields = ["input","button","a"]
        out = {}
        for field in self.fields:
            if field not in out.keys():
                out[field] = self.get_fields(field)
            else:
                count = list(out.keys()).count(field)
                out[field + str(count)] = self.get_fields(field)
        return out

    def get_inputs(self):
        return self.get_all()["input"]

    def get_links(self):
        return self.get_all()["a"]

    def get_buttons(self):
        return self.get_all()["button"]

    def get_input_list(self):
        return list(self.get_inputs().keys())
    
    def get_button_list(self):
        return list(self.get_buttons().keys())
    
    def get_link_list(self):
        return list(self.get_links().keys())

    def get_clue_list(self):
        out = self.get_input_list() + self.get_button_list() + self.get_link_list()
        return out
        
    def clear(self,webelement):
        webelement.clear()
    
    def write(self,webelement,text):
        self.clear(webelement)
        webelement.send_keys(text)
    
    def submit(self,webelement,text):
        self.write(webelement,text)
        webelement.send_keys(Keys.ENTER)
    
    def get_element(self,clue):
        keys = ["aria-label","name","placeholder","id","a"]
        for field in keys:
            all_the_fields = self.get_all()[field]
            for clues in all_the_fields:
                if clues==clue:
                    return all_the_fields[clue]
    
    def click(self,webelemenet,max_time=100):
        webelemenet.click()

    def get_images(self):
        links = []
        imgs = driver.find_elements(By.TAG_NAME,"img")
        for img in imgs:
            link = img.get_attribute("src")
            if link!=None and link.startswith("http"):
                links.append(link)
        return links

    

class WeBAutomator(Page):
    def __init__(self):
        global driver
        driver = Chrome(service=Service(cm().install()))

    def open(self,url):
        super().__init__(url)

    def maximize(self):
        driver.maximize_window()

    def minimize(self):
        driver.minimize_window()
    
    def close(self):
        driver.quit()
