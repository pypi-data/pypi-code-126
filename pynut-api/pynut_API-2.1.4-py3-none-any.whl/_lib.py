#-----------------------------------------------------------------
# pynut
#-----------------------------------------------------------------
def nutOther():
    try:
        from pyNutTools import nutOther
    except Exception as err:
        print('  IMPORT FAIL |nutOther|, err:|{}|'.format(err))
        return None
    return nutOther


#-----------------------------------------------------------------
# Generic Lib
#-----------------------------------------------------------------
def logging():
    try:    import logging
    except Exception as err:
        print('  IMPORT FAIL |logging|, err:|{}|'.format(err))
        return None
    return logging

def logger():
    try:
        import logging
        logger = logging.getLogger()
    except Exception as err:
        print('  IMPORT FAIL |logger|, err:|{}|'.format(err))
        return None
    return logger


#-----------------------------------------------------------------
# dataframe
#-----------------------------------------------------------------
def numpy():
    try:    import numpy
    except Exception as err:
        print('  IMPORT FAIL |numpy|, err:|{}|'.format(err))
        return None
    return numpy

def pandas():
    try:    import pandas
    except Exception as err:
        print('  IMPORT FAIL |pandas|, err:|{}|'.format(err))
        return None
    return pandas


# #-----------------------------------------------------------------
# # Date
# #-----------------------------------------------------------------
# def datetime():
#     try:    import datetime
#     except Exception as err:
#         print('  IMPORT FAIL |datetime|, err:|{}|'.format(err))
#         return None
#     return datetime
#
# def dateutil():
#     try:    import dateutil
#     except Exception as err:
#         print('  IMPORT FAIL |dateutil|, err:|{}|'.format(err))
#         return None
#     return dateutil
#
# def timezone():
#     try:    from datetime import timezone
#     except Exception as err:
#         print('  IMPORT FAIL |timezone|, err:|{}|'.format(err))
#         return None
#     return timezone
#
# def BDay():
#     try:    from pandas.tseries.offsets import BDay
#     except Exception as err:
#         print('  IMPORT FAIL |BDay|, err:|{}|'.format(err))
#         return None
#     return BDay
#
# def relativedelta():
#     try:    from dateutil.relativedelta import relativedelta
#     except Exception as err:
#         print('  IMPORT FAIL |relativedelta|, err:|{}|'.format(err))
#         return None
#     return relativedelta



#-----------------------------------------------------------------
# API
#-----------------------------------------------------------------
def re():
    try:    import re
    except Exception as err:
        print('  IMPORT FAIL |re|, err:|{}|'.format(err))
        return None
    return re

def requests():
    try:    import requests
    except Exception as err:
        print('  IMPORT FAIL |requests|, err:|{}|'.format(err))
        return None
    return requests

def BeautifulSoup():
    try:    from bs4 import BeautifulSoup
    except Exception as err:
        print('  IMPORT FAIL |BeautifulSoup|, err:|{}|'.format(err))
        return None
    return BeautifulSoup

def urlopen():
    try:    from urllib.request import urlopen
    except Exception as err:
        print('  IMPORT FAIL |urlopen|, err:|{}|'.format(err))
        return None
    return urlopen

def urlretrieve():
    try:    from urllib.request import urlretrieve
    except Exception as err:
        print('  IMPORT FAIL |urlretrieve|, err:|{}|'.format(err))
        return None
    return urlretrieve

def unicodedata():
    try:    import unicodedata
    except Exception as err:
        print('  IMPORT FAIL |unicodedata|, err:|{}|'.format(err))
        return None
    return unicodedata

def selenium():
    try:    import selenium
    except Exception as err:
        print('  IMPORT FAIL |selenium|, err:|{}|'.format(err))
        return None
    return selenium

def selenium_webdriver():
    try:    from selenium import webdriver as selenium_webdriver
    except Exception as err:
        print('  IMPORT FAIL |selenium_webdriver|, err:|{}|'.format(err))
        return None
    return selenium_webdriver


