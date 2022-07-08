from django.http.response import HttpResponse
import numpy as np
import json
import base64

from .processing import GetTemplateGuidFromPath
from .mka_requests import ParamsMapper
from .base64_converter import Base64Converter
from .services_managment import ServiceController,Services

class RequestParser():
    DICTIONARY_LIST_TYPE=ParamsMapper.DICTIONARY_LIST_TYPE
    def __init__(self,req,expected_keys_list) -> None:
        # self._request_files=req.FILES.getlist('files')
        self._passed_request=req
        self._expected_keys=ParamsMapper.GetParamsMappingsDictionary(expected_keys_list)
        self._request_dict=dict()
        self._error=dict()
        

    def ParseRequest(self):
        self._request_dict=self._passed_request.data

        requestContentType=self._passed_request.META['CONTENT_TYPE']
        if requestContentType=="application/json":
            stauts,response=self._JsonRequestLoader()
        else:
            stauts,response=self._FormDataRequestLoader()
        

        if not stauts:
            self._error=response
        else:
            self._request_dict=response

        return stauts


    def _JsonRequestLoader(self):

        status,response=self._ValidateRequest()
        return status,response
    

    # return body



    def _FormDataRequestLoader(self):

        self._passed_request.data._mutable=True

        # self._passed_request.query_params.gitlist("file_path_info")
        foundKeys=np.intersect1d(list(self._request_dict.keys()),list(self._expected_keys.keys()))
        self._request_dict=self._passed_request.data.copy()
        for key in foundKeys:
            properties=self._expected_keys[key]
            if properties["type"]==self.DICTIONARY_LIST_TYPE :
                keyValues=self._passed_request.data.getlist(key)
                print(keyValues)
                if isinstance(keyValues,str):
                    keyValues=[json.loads(keyValues)]
                else:
                    for dict_str in keyValues:
                         dict_str=json.loads(dict_str)
                self._request_dict[key]=keyValues
                print(self._request_dict[key])
            elif properties["type"]==list:
                self._request_dict[key]=self._request_dict.getlist(key)
            elif properties["type"]==dict:
                self._request_dict[key]=json.loads(self._request_dict[key])
            elif properties["type"]==bool:
                self._request_dict[key]=json.loads(self._request_dict[key].lower())
            else:
                self._request_dict[key]=properties["type"](self._request_dict[key])
                continue
            # if isinstance(self._request_dict[key]["type"]
        # for key,value in passedFormData.items():
        #     self.passedFormData[key]=str(value) if self._expected_keys[key]=="String" else int(value) if self._expected_keys[key]=="Number" else float(value) if self._expected_keys[key]=="Decimal" else str(value) if self._expected_keys[key]=="String"
        
        status,validation_response=self._ValidateRequest()
        self._passed_request.data._mutable=False
        return status,validation_response


    def _ValidateRequest(self):
        requestkeys=self._request_dict.keys()
        notFoundKeysInRequest=[]
        for key,value in self._expected_keys.items():
            if key in requestkeys:
                if value["type"]==self.DICTIONARY_LIST_TYPE:
                    try:
                        self._request_dict[key]=self._request_dict[key]
                    except:
                        example=value.get("example")
                        notFoundKeysInRequest.append(f"{key}:value like {example}")
                    continue

                elif value["type"]==dict:
                    if isinstance(self._request_dict[key],dict):
                        continue
                    else:
                        notFoundKeysInRequest.append(f"{key}:should be map key:value")
                        continue
                elif value["type"]==list:
                    if not isinstance(self._request_dict[key],list):
                        notFoundKeysInRequest.append(f"{key}:should be list")
                    if "values" in value.keys():
                        for keyValue in self._request_dict[key]:
                            if keyValue not in value["values"] :
                                notFoundKeysInRequest.append(f"{key} values should be in {'or'.join(i for i in value['values'])}")
                                break
                elif value["type"]==dict:
                    if not isinstance(self._request_dict[key],dict):
                        notFoundKeysInRequest.append(f"{key}:should be map key:value")

                elif value["type"]==bool:
                    if not isinstance(self._request_dict[key],dict):
                        notFoundKeysInRequest.append(f"{key}:should be boolean True,False")
                elif value["type"]==any:
                    continue
                else:
                    print(self._request_dict[key],value["type"])
                    if not isinstance(self._request_dict[key],value["type"]):
                        notFoundKeysInRequest.append(f"{key}:should be {'number' if value['type']==int else 'decimal' if value['type']==float else 'text'}")
                    self._request_dict[key]=value["type"](self._request_dict[key])
                    continue
            elif value["has_default"]:
                self._request_dict[key]=value["default"]
            else:
                notFoundKeysInRequest.append(key)

        return True if len(notFoundKeysInRequest)==0 else False,self._request_dict if len(notFoundKeysInRequest)==0 else notFoundKeysInRequest

    def ReadListFiles(self):
        passedFiles=self._passed_request.FILES.getlist("files",[])
        passedFilesData=[]
        if passedFiles!=[]:
            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.UPLOAD_FILES_FROM_SERVICE,self._passed_request,Services.DATA_KEY)
            if not status:
                return response

            passedFilesData.extend(response)


        if self._request_dict["file_path_info"] is not None and self._request_dict["file_path_info"] !=[] :

            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.READ_DF_FILE_FROM_SERVICE,{"file_path_info":self._request_dict["file_path_info"]},Services.DATA_KEY)
            if not status:
                return response
    
            passedFilesData.extend(response)

        for file in passedFilesData:
            file.update({"template_guid":GetTemplateGuidFromPath["file_path"]})
        return passedFiles

    def ReadFile(self,file_path_info={}):
        
        passedFiles=None if file_path_info=={} else self._passed_request.FILES.get("files",None)
        passedFilesData=[]
        if passedFiles is not None:
            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.FILE_SERVICE_NAME,Services.UPLOAD_FILES_FROM_SERVICE,{"files":base64.b64encode(self._passed_request.FILES.get("files").read()).decode()},Services.DATA_KEY)
            if not status:
                return response
            
            response[0].update({"template_guid":GetTemplateGuidFromPath(response[0]["file_path"])})
            return response[0]


        fileToRead=file_path_info["file_path_info"] if file_path_info!={} else self._request_dict["file_path_info"] 
        status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.FILE_SERVICE_NAME,Services.READ_DF_FILE,{"file_path_info":fileToRead[0:1] if isinstance(fileToRead,list) else [fileToRead]},Services.DATA_KEY)
        if not status:
            return response
        
        response[0].update({"template_guid":GetTemplateGuidFromPath(response[0]["file_path"])})
        return response[0]

    def ReadMediaFiles(self):
        
        passedFiles=self._passed_request.FILES.get("files",None)

        passedFilesData=[]
        if passedFiles is not None:
            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.UPLOAD_FILES_FROM_SERVICE,self._passed_request.FILES.get("files"),Services.DATA_KEY)
            if not status:

                return False,response
            passedFilesData.extend(response)

        if self._request_dict["file_path_info"] is not None or self._request_dict["file_path_info"] !=[] :
            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.READ_MEDIA_FILE,{"file_path_info":self._request_dict["file_path_info"]},Services.DATA_KEY)
            if not status:

                return False,response
            if not status:
                return False,response
            
            passedFilesData.extend(response)

        return True,passedFilesData 




    @staticmethod
    def SaveDfInFile(df,extension=".csv",sheet=None,template_guid=None):
        df_as_json=df.to_json(orient='records')
        serviceCallStatus,serviceCallResults= ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.SAVE_DF_DATA_IN_FILE,data={"json_data":df_as_json,"extension":extension,"sheet":sheet,"template_guid":template_guid},response_key=Services.FILE_KEY)
        if not serviceCallStatus:
                return False,{'message':serviceCallResults["message"],"code":422}
        outfilename=serviceCallStatus
        return True,outfilename

    def ReadPickle(self,pickle_path:str,pickle_type="model"):
        serviceController=ServiceController(Services.FILE_SERVICE_NAME)
        serviceCallResults= serviceController.CallEurekaService(Services.LOAD_PICKLE,data={"pickle_path":pickle_path,"pickle_type":pickle_type},response_key=Services.DATA_KEY)

        if not serviceCallResults:
                return False,{'message':serviceCallResults["message"],"code":422}
        readResult=serviceController._response_data
        readResult[pickle_path]=Base64Converter.B64ToPickle(readResult[str(pickle_path)])
        if "TransformersObjects" in readResult.keys() and readResult["TransformersObjects"]!={}:
            transformerObjects=readResult["TransformersObjects"]
            for pickle_name,pickle_b64 in transformerObjects.items():
                transformerObjects[pickle_name]=Base64Converter.B64ToPickle(pickle_b64)
        return True,readResult
    def ReturnErrorMessage(self,error_message=None):
        if not error_message:
            return HttpResponse(json.dumps({'status': False, 'message': ",".join(i for i in self._error)}), status=422,
                                        content_type='application/json')
        else :
            return HttpResponse(json.dumps({'status': False, 'message': error_message["message"]}),status=error_message["code"],
                                        content_type='application/json')






class ParamsMapper:
    DICTIONARY_LIST_TYPE="DictionaryList"

    _key_for_all_requests={

            "file_path_info": {"type":DICTIONARY_LIST_TYPE,"has_default":True,"default":[]},
            "keywords_count": {"type":int,"has_default":True,"default":4},
            "keywords_algorithms": {"type":list,"has_default":True,"default":["YAKE"]},
            "sentiment_option": {"type":dict,"has_default":True,"default":{"name": "Text", "value": None}},
            "cleaning_codes": {"type":dict,"has_default":True,"default":{}},
            "forbidden_words": {"type":dict,"has_default":True,"default":{}},
            "content_language": {"type":str,"has_default":True,"default":"en"},
            "selected_analysis_type": {"type":list,"has_default":False},
            "summary_algorithm": {"type":list,"has_default":True,"default": ["LEX_RANK"]},
            "minimizing_approach": {"type":dict,"has_default":True,"default": {'action': 'numberOfBestSentences', 'value': 5}},
    }

    @staticmethod
    def GetParamsMappingsDictionary(expected_keys_list):
        return {key:ParamsMapper._key_for_all_requests.get(key) for key in expected_keys_list}