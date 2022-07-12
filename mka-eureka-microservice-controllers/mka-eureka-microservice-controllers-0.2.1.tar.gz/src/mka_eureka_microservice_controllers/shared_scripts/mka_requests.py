from django.http.response import HttpResponse
import numpy as np
import json
import base64

from .mka_processing import GetTemplateGuidFromPath
from .mka_base64_converter import Base64Converter
from .mka_services_managment import ServiceController,Services

class ParamsMapper(object):
    DICTIONARY_LIST_TYPE="DictionaryList"

    _key_for_all_requests={
            ######################## for all services ########################
            "file_path_info": {"type":DICTIONARY_LIST_TYPE,"has_default":True,"default":[]},
            "sheet":{"type":any,"has_default":True,"default":None},


            #########################******* for text analysis service *******########################
            "keywords_count": {"type":int,"has_default":True,"default":4},
            "keywords_algorithms": {"type":list,"has_default":True,"default":["YAKE"]},
            "sentiment_option": {"type":dict,"has_default":True,"default":{"name": "Text", "value": None}},
            "cleaning_codes": {"type":dict,"has_default":True,"default":{}},
            "forbidden_words": {"type":dict,"has_default":True,"default":{}},
            "content_language": {"type":str,"has_default":True,"default":"en"},
            "selected_analysis_type": {"type":list,"has_default":False},
            "summary_algorithm": {"type":list,"has_default":True,"default": ["LEX_RANK"]},
            "minimizing_approach": {"type":dict,"has_default":True,"default": {'action': 'numberOfBestSentences', 'value': 5}},
            
            
            ########################******* for machine learning service ********########################

            #++++++++++++++++++++++++++++++ fit model ++++++++++++++++++++++++++++++#
            
            "features": {"type": list,"has_default":False},
            "algorithms": {"type": list,"has_default":True,"default":[]},
            "ml_method": {"type": str,"values":["Regression","Classification","Clustering"],"has_default":False},
            "auto_select_algorithms": {"type": bool,"has_default":False},



            #++++++++++++++++++++++++++++++ Predictive(Classification,Regression) Train ++++++++++++++++++++++++++++++#

            "label":{"type":str,"has_default":False},
            "split_mechanism": {"type": str,"values":['k_fold','random'],"has_default":True,"default":"random"},
            "train_size": {"type": float,"has_default":False},
            "count_of_folds": {"type": int,"has_default":False,"default":5},
            "continuous_target_to_discrete": {"type": bool,"has_default":True,"default":False},
            "contiuous_encoding": {"type": bool,"has_default":True,"default":False},
            "remove_to_many_values": {"type": bool,"has_default":True,"default":False},
            "extract_date_info": {"type":bool,"has_default":True,"default":False},



            #++++++++++++++++++++++++++++++ Non-Predictive(Clustering) Train ++++++++++++++++++++++++

            "min_clusters": {"type": int,"has_default":True,"default":2},
            "max_clusters": {"type": int,"has_default":True,"default":20},
            "fully_tree": {"type": bool,"has_default":True,"default":False},



            #++++++++++++++++++++++++++++++ Predict Values ++++++++++++++++++++++++++++++#

            "predict_data": {"type":DICTIONARY_LIST_TYPE,"attributes":["Name","value"],"has_default":False},
            "model_path": {"type": str,"has_default":False},


            #++++++++++++++++++++++++++++++ Change Clustering Groups names ++++++++++++++++++++++++++++++#

            "clusters_map": {"type":dict,"has_default":False},
            "clusters_column": {"type":any,"has_default":True,"default":None},



            #++++++++++++++++++++++++++++++ Model Optmization(Clustering,Classification) ++++++++++++++++++++++++++++++#

            "class_to_optimize_for": {"type":any,"has_default":False},
            "dir_for_conf": {"type":str,"has_default":True,"default":"Maximize"},
            "constrains": {"type":str,"has_default":True,"default":""},
            "stay_within": {"type":bool,"has_default":True,"default":False},
            "stay_below": {"type":bool,"has_default":True,"default":True},
            "stay_above": {"type":bool,"has_default":True,"default":True},
            "stay_within_num": {"type":any,"has_default":True,"default":None}
    }
    @classmethod

    def GetParamsMappingsDictionary(cls,expected_keys_list):
        return {key:ParamsMapper._key_for_all_requests.get(key) for key in expected_keys_list}
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
                convertedValues=[]
                for dict_str in keyValues:
                        dict_str=json.loads(dict_str)
                        convertedValues.append(dict_str)
                self._request_dict[key]=convertedValues

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
        print(validation_response)
        return status,validation_response


    def _ValidateRequest(self):

        requestkeys=self._request_dict.keys()
        notFoundKeysInRequest=[]
        for key,value in self._expected_keys.items():
            if key in requestkeys:
                if value["type"]==self.DICTIONARY_LIST_TYPE:

                        # example=value.get("example")
                        # notFoundKeysInRequest.append(f"{key}:value like {example}")
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
                    if not isinstance(self._request_dict[key],bool):
                        notFoundKeysInRequest.append(f"{key}:should be boolean True,False")
                elif value["type"]==any:
                    continue
                else:
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
            status,response=ServiceController.CallEurekaService(service_name=Services.FILE_SERVICE_NAME,service_url=Services.UPLOAD_FILES_FROM_SERVICE,data=self._passed_request,response_key=Services.DATA_KEY)
            if not status:
                return response

            passedFilesData.extend(response)


        if self._request_dict["file_path_info"] is not None and self._request_dict["file_path_info"] !=[] :

            status,response=ServiceController.CallEurekaService(service_name=Services.FILE_SERVICE_NAME,service_url=Services.READ_DF_FILE_FROM_SERVICE,data={"file_path_info":self._request_dict["file_path_info"]},response_key=Services.DATA_KEY)
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
            status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.UPLOAD_FILES_FROM_SERVICE,Services.UPLOAD_FILES_FROM_SERVICE,data={"files":base64.b64encode(self._passed_request.FILES.get("files").read()).decode()},response_key=Services.DATA_KEY)
            if not status:
                return response
            
            response[0].update({"template_guid":GetTemplateGuidFromPath(response[0]["file_path"])})
            return response[0]


        fileToRead=file_path_info["file_path_info"] if file_path_info!={} else self._request_dict["file_path_info"] 
        status,response=ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.READ_DF_FILE,data={"file_path_info":fileToRead[0:1] if isinstance(fileToRead,list) else [fileToRead]},response_key=Services.DATA_KEY)
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
    def SaveDfInFile(cls,df,extension=".csv",sheet=None,template_guid=None):
        df_as_json=df.to_json(orient='records')
        serviceCallStatus,serviceCallResults= ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.SAVE_DF_DATA_IN_FILE,data={"json_data":df_as_json,"extension":extension,"sheet":sheet,"template_guid":template_guid},response_key=Services.FILE_KEY)
        if not serviceCallStatus:
                return False,{'message':serviceCallResults["message"],"code":422}
        outfilename=serviceCallStatus
        return True,outfilename

    def ReadPickle(self,pickle_path:str,pickle_type="model"):
        serviceCallResults,serviceCallResponse= ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.LOAD_PICKLE,data={"pickle_path":pickle_path,"pickle_type":pickle_type},response_key=Services.DATA_KEY)

        if not serviceCallResults:
                return False,{'message':serviceCallResults["message"],"code":422}
        serviceCallResponse[pickle_path]=Base64Converter.B64ToPickle(serviceCallResponse[str(pickle_path)])
        if "TransformersObjects" in serviceCallResponse.keys() and serviceCallResponse["TransformersObjects"]!={}:
            transformerObjects=serviceCallResponse["TransformersObjects"]
            for pickle_name,pickle_b64 in transformerObjects.items():
                transformerObjects[pickle_name]=Base64Converter.B64ToPickle(pickle_b64)
        return True,serviceCallResponse
    def ReturnErrorMessage(self,error_message=None):
        if not error_message:
            return HttpResponse(json.dumps({'status': False, 'message': ",".join(i for i in self._error)}), status=422,
                                        content_type='application/json')
        else :
            return HttpResponse(json.dumps({'status': False, 'message': error_message["message"]}),status=error_message["code"],
                                        content_type='application/json')





