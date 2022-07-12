from dataclasses import dataclass
from distutils.log import error
import sys, getopt
import os
from unittest import mock
from wsgiref.headers import Headers        
import dotenv
from numpy import source 
import requests
import json
import yaml
from munch import Munch
from .log_management import log_management

errorDualLogger = log_management.get_error_dual_logger()
infoDualLogger = log_management.get_info_dual_logger()

class mockapi():

    def mockit(config):
        with open(config) as f:
             cfg = yaml.safe_load(f)
        ## if is Auth is true then its auth token service, only work on auth token and break

        if cfg['workflows']['flow']['source']['isAuthOnly'] :
                payload = class_instance.getAuth(cfg)
        else:
                payload = class_instance.getData(cfg)
 
        return payload
        
    # get Data Function for the give Source end point
    def getData(self,cfg):
        payload=""
        auth_payload = json.loads(class_instance.getAuth(cfg))
        
        url = cfg['workflows']['flow']['source']['request']['api-endpoint']      
        
        querylist={}
     
        if(cfg['workflows']['flow']['source']['request']['params'] is not None):
            for x in cfg['workflows']['flow']['source']['request']['params']:
                querylist.update(x)
        
        queryParams = str(querylist)
        replacedquery = queryParams.replace('\'','"')
        infoDualLogger.info(f"Queries: {replacedquery}")
        token =auth_payload.get("access_token")

        headerlist = {'Authorization': "Bearer {}".format(token)}
        
        for y in cfg['workflows']['flow']['source']['request']['headers']:
            headerlist.update(y)

        payload =  cfg['workflows']['flow']['source']['request']['body']
        response = requests.request(cfg['workflows']['flow']['source']['request']['method'], url, headers= headerlist, data=payload)
        if response.status_code == 200:
            infoDualLogger.info(f"Response Code from URL {url} is 200 OK")
        else:
            errorDualLogger.error(f"Error: Response Code from URL {url} is {response.status.code}.")
        return response.text

    # Get Authorization Function
    def getAuth(self,cfg):  
        url = cfg['workflows']['flow']['source']['auth-endpoint']
        infoDualLogger.info(f"Getting Token from Auth Token URL {url}")
        payload = ""         
        headers = { }
        for var in cfg['workflows']['flow']['source']['headers']:
             headers = var
        response = requests.request("POST", url, headers=headers, data=payload)
        infoDualLogger.info(f"Response Code from URL {url} is {response.status_code} OK")
        if response.status_code == 200:
            return response.text
        else:
            errorDualLogger.error(f"Received Error from Auth Service {response.status_code}")
            exit()
        
class_instance = mockapi()
