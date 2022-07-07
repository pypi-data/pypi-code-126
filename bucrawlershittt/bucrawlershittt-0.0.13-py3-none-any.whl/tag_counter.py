import requests
from builtins import property



class Tags_Counter:
    def __init__(self):
        self.__url      = 'https://shawkialaddin.com' # target url
        self.__tags     = [] # target tags
        self.__src      = None
        self.__resualt  = {}


    @property
    def url(self):
        return self.__url
    
    
    @url.setter
    def url(self,url):
        url='https://'+url  if url[0:3] != 'http' else url
        self.__url = url
            
        
    @property
    def tags(self):
        return self.__tags
    
    
    @tags.setter
    def tags(self,tags):
        self.__tags = tags
            
        
    def __get_src(self):
        req = requests.get(self.__url)
        self.__src = req.text
        
            
    @property
    def count_tags(self):
        self.__get_src()
        for tag in self.__tags:
            self.__resualt[f'{tag}'] = self.__src.count(tag)
        return self.__resualt