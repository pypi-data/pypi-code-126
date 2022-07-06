import sys, os, re, requests, json, yaml
from tabulate import tabulate
from .log_management import log_management
from .otbctl_main  import otbcli
from .otbctl_mock import mockapi
from .yaml_validate import validate_config

errorDualLogger = log_management.get_error_dual_logger()
infoDualLogger = log_management.get_info_dual_logger()
infoFileLogger = log_management.get_info_file_logger()
context = otbcli.getContext('otbctl-context')

class testbed():

    def allMocks():
        try:
            server_url = context +"/mocks"
        except TypeError:
            errorDualLogger.error("Context must be set first. usage: otbctl setcontext")
            exit()
        try:
            response = requests.get(server_url)
        except:
            errorDualLogger.error("Error: failed to connect to server.")
            exit()
        if response.status_code == 400:
            errorDualLogger.error(f'400 response from server {response.url}')
            sys.exit
        elif response.status_code == 200:
            responsedata = response.json() 
            if(responsedata == 0):
                infoDualLogger.info("No Mocks are registered")
            else:
                return response.json()

    def getMocks():
        mocks_table = []
        if len(testbed.allMocks()) == 0:
            infoDualLogger.info("No mocks found on server.")
            infoDualLogger.info("Usage: 'otbctl -h' for help.")
        else:
            for mock in testbed.allMocks():
                mock_row = []
                state = mock['state']['id']
                path = mock['request']['path']['value']
                creation = mock['state']['creation_date']
                method = mock['request']['method']['value']
                locked = mock['state']['locked']
                mock_row.extend([state, path, method, locked, creation])
                mocks_table.append(mock_row)
            infoDualLogger.info(tabulate(mocks_table, headers=["\nMockID", "\nPath", "\nMethod", "\nLocked?", "\nCreation"]))

    def getMockbyID(id):
        server_url = context +"/mocks?id="+id
        method='GET'
        response = requests.get(server_url)

        if response.status_code == 400:
            errorDualLogger.error(f'Response: 400 Not Found {response.url}')
            sys.exit
        elif response.status_code == 200:  
            infoDualLogger.info('Response: 200 OK') 
            responsedata = response.json()
            if( responsedata == 0):
                infoDualLogger.info("No Mocks are registered")
            else:
                infoDualLogger.info(f'{json.dumps(response.json(), indent=4)}')

    def addMock(config_yamls):
        try:
            server_url = context +"/mocks"
        except TypeError:
            errorDualLogger.error("Context must be set first. usage: otbctl setcontext")
            exit()
        if config_yamls[0] == '.':
            if len(config_yamls) > 1: # prevents 'otbctl add -f . foo bar'
                infoDualLogger.info("Usage: 'otbctl add -f' plus file name(s), or 'otbctl add -f .' for all mocks in current directory.")
                exit()
            else:
                config_yamls = [] # remove '.', add files.
                for filename in os.listdir():
                    config_yamls.append(filename)
        for file in config_yamls:
            validate_config(file)
            method='POST'
            # getdatafromapi='{"access_token":"d6ac8cff-3807-364c-97c5-7b3f312cb054","scope":"am_application_scope default","token_type":"Bearer","expires_in":464}"'
            getdatafromapi = mockapi.mockit(file)
            infoFileLogger.info(f"Received data from Configured end point {getdatafromapi}")
            
            payload = class_instance.buildPayload(getdatafromapi, file)
            
            headers = {
                'Content-Type': 'application/json'
            }
            try:
                response = requests.request(method, server_url, headers=headers, data=payload)
            except UnicodeEncodeError:
                errorDualLogger.error(f"Error: part of response body from {getdatafromapi} was invalid.")
            infoFileLogger.info(response.text)

    def buildPayload(self, payload, config_yaml):
        replacedString = payload.replace('\\"','\\\\"')
        replacedString = replacedString.replace('"','\\"')
        replaceadditional = replacedString.replace('\\\\"','\\\\"')
        
        with open(config_yaml) as f:
             cfg = yaml.safe_load(f)

        status = cfg['workflows']['flow']['testbed']['request']['status']
        converted_num = f'{status}'
        
        querylist={}
        if(cfg['workflows']['flow']['testbed']['request']['params'] is not None):
            for x in cfg['workflows']['flow']['testbed']['request']['params']:
                querylist.update(x)
        queryParams = str(querylist)
        replacedquery = queryParams.replace('\'','"')

        headerlist={}
        if(cfg['workflows']['flow']['testbed']['request']['headers'] is not None):
            for y in cfg['workflows']['flow']['testbed']['request']['headers']:
                headerlist.update(y)
        replacedHeaders = str(headerlist).replace('\'','"')
     
        if(cfg['workflows']['flow']['testbed']['request']['body'] is not None):
           replacedBody = cfg['workflows']['flow']['testbed']['request']['body'].replace('"','\\"')
           replacedNewLine= replacedBody.replace('\n','\\n')
        
        if(cfg['workflows']['flow']['testbed']['request']['method'] =='POST'):
            jsonString ='[{"request": { "method": "'+cfg['workflows']['flow']['testbed']['request']['method']+'","path": "'+cfg['workflows']['flow']['testbed']['request']['path']+'","body":"'+ replacedNewLine+'"},"response": { "status": '+converted_num +',"headers":' + replacedHeaders+',"body": "' +replaceadditional+ '"}}]'
        else:
            jsonString ='[{"request": { "method": "'+cfg['workflows']['flow']['testbed']['request']['method']+'","path": "'+cfg['workflows']['flow']['testbed']['request']['path']+'","query_params":'+replacedquery+'},"response": { "status": '+converted_num +',"headers":' + replacedHeaders+',"body": "' +replaceadditional+ '"}}]'
    
        infoFileLogger.info(jsonString)
        return jsonString

    def load(mock_data):
        if mock_data[0] == '.':
            if len(mock_data) > 1: # prevents 'otbctl load -f . foo bar'
                infoDualLogger.info("Usage: 'otbctl load -f' plus file name(s), or 'otbctl load -f .' for all mocks in current directory.")
                exit()
            else:
                mock_data = [] # remove '.', add files.
                for filename in os.listdir():
                    mock_data.append(filename)
        for file in mock_data:
            infoDualLogger.info(f'Loading Mocks from File -> {file}')
            try:
                server_url = context +"/mocks"
            except TypeError:
                errorDualLogger.error("Context must be set first. usage: otbctl setcontext")
                exit()
            method='POST'
            try:
                filereader = open(file, 'r')
            except FileNotFoundError:
                errorDualLogger.error(f"Mock data file {file} not found")
                continue
            regexMatch = re.search('^\[\{\\\"request\\\"\:', filereader.readline())
            if regexMatch is None: # validating file contents then file type.
                errorDualLogger.error(f"Error: JSON file {file} is formatted incorrectly.")
                continue
            elif not file.endswith(".json"):
                errorDualLogger.error(f"Error: File type of {file} must be JSON.")
                continue
            Lines = filereader.readlines()
            count = 0
            # Strips the newline character
            for line in Lines:
                count += 1
                payload = line.strip()
                jsonRe = json.dumps(payload)
                infoFileLogger.info(f"Adding Mock to mock server.....{jsonRe}")
                headers = {
                    'Content-Type': 'application/json'
                }
            # response = requests.request(method, server_url, headers=headers, data=payload)
            # infoDualLogger.info(response.text)

    def delMocks():
        try:
            server_url = context +"/reset"
        except TypeError:
            errorDualLogger.error("Context not set, no mocks to delete. usage: otbctl setcontext")
            exit()
        response = requests.request("POST", server_url)
        if response.status_code == 400:
            errorDualLogger.error(f'400 response from server {response.url}')
            sys.exit
        elif response.status_code == 200:  
            infoDualLogger.info('200 OK') 
            infoDualLogger.info(response.text)
    
    def lockMock(mock_ids):
        if '.' in mock_ids:
            if len(mock_ids) > 1:
                infoDualLogger.info("Usage: 'otbctl lock -m' with mock IDs or . for all mocks.")
                exit()
            else:
                mock_ids = [] # remove '.'
                for mock in testbed.allMocks(): # add all mock IDs on server to list
                    mock_ids.append(mock['state']['id'])
        try:
            server_url = context + "/mocks/lock"
        except:
            errorDualLogger.error("Context must be set first. usage: otbctl setcontext")
        response = requests.post(server_url, json=mock_ids)
        if response.status_code == 400:
            errorDualLogger.error(f'400 response from server {response.url}')
            sys.exit
        elif response.status_code == 200:  
            infoDualLogger.info(f"Locking mock ID(s): {mock_ids}")
            infoDualLogger.info("Locked mocks are protected from 'otbctl reset all' command.\nRun 'otbctl get' to see locked status for all mocks.")

    def unlockMock(mock_ids):
        if '.' in mock_ids:
            if len(mock_ids) > 1:
                infoDualLogger.info("Usage: 'otbctl unlock -m' with mock IDs or . for all mocks.")
                exit()
            else:
                mock_ids = [] # remove '.'
                for mock in testbed.allMocks(): # add all mock IDs on server to list
                    mock_ids.append(mock['state']['id'])
        try:
            server_url = context + "/mocks/unlock"
        except:
            errorDualLogger.error("Context must be set first. usage: otbctl setcontext")
        response = requests.post(server_url, json=mock_ids)
        if response.status_code == 400:
            errorDualLogger.error(f'400 response from server {response.url}')
            sys.exit
        elif response.status_code == 200:  
            infoDualLogger.info(f"Unlocking mock ID(s): {mock_ids}")
            infoDualLogger.info("Unlocked mocks can be reset with 'otbctl reset all'.\nRun 'otbctl get' to see locked status for all mocks.")
    
class_instance = testbed()