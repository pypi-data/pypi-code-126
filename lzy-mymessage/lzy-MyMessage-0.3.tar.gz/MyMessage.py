import requests
from lxml import etree
import ListConversionDictionary

def MyMessage(key):
    tree = etree.HTML(requests.get('https://edgeip.lofter.com/').text)
    hrefs = tree.xpath('//*[@id="main"]/div/div/div[2]/a[2]/@href')
    dictionary = {}
    for href in hrefs:
        data = etree.HTML(requests.get(href).text)
        key_cell = data.xpath('//*[@id="main"]/div[1]/div/h2/a/text()')
        value_cell = data.xpath('//*[@id="main"]/div[1]/div/div[1]/p/text()')
        data_list = ListConversionDictionary.ListConversionDictionary(key_cell,value_cell)
        if data_list:
            dictionary.update(data_list)
    return dictionary.get(key)