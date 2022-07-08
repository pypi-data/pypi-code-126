from django.http import HttpResponse
import py_eureka_client.eureka_client as eureka_client
import json


POST_REQUEST_TYPE="POST"
GET_REQUEST_TYPE="GET"

SERVICES_CONTEXT={
    "READ_FILE":["file_path_info"],
}

class Services():
    
    FILE_SERVICE_NAME="FileService"
    EDA_SERVICE_NAME="EDA-Service"
    DM_SERVICE_NAME="DataMinning-Service"
    DATABASE_SERVICE_NAME="DbController-Service"
    # DM_SERVICE="read_data/from_file/"
    READ_DF_FILE="read_data/from_file/"
    READ_MEDIA_FILE="read_data/from_media_from_service/"
    READ_DF_FILE_FROM_SERVICE="read_data/from_file_from_service/"
    READ_DF_FILE_RESPONSE_KEY="json_data"
    READ_DF_FILE_WITH_PAGINATION="read_data/from_file_with_pagination/"
    READ_DF_FILE_WITH_PAGINATION_RESPONSE_KEY="json_data"
    READ_DF_FILE_WITH_SUBCOLUMNS="read_data/from_file_with_subcolumns/"
    READ_DF_DATA_WITH_FROM_DB="read_data/from_db/"
    SAVE_DF_DATA_IN_FILE="read_data/save_file/"
    UPLOAD_FILES_FROM_SERVICE="read_data/upload_bulk_from_service/"
    SAVE_PICKLE="pickle/save_pickle/"
    FILE_KEY="file_guid"
    LOAD_PICKLE="pickle/load_pickle/"
    JSON_DATA_KEY="json_data"
    DATA_KEY="data"



class ServiceController():
    

    # def __init__(self,service_name=FILE_SERVICE) -> None:
    #     super.__init__()
    #     self._service_name=service_name
    #     self._service_tag=None
    #     self._request_type=None
    #     self._response_data=None
    #     self._response_error=None
    
    @staticmethod

    def CallEurekaService(service_name,service_url:str,data:dict,response_key:str,request_type=POST_REQUEST_TYPE):
        print("eureka call to ",service_url)
        # self._service_tag=service_url
        if service_url==Services.UPLOAD_FILES_FROM_SERVICE:

            serviceCallResults= json.loads(eureka_client.do_service(service_name,service_url,data=data,method=request_type))
        else:
            serviceCallResults= json.loads(eureka_client.do_service(service_name,service_url,data=json.dumps(data),method=request_type))
        if serviceCallResults["status"] == False:
                return False,{'message':serviceCallResults["message"],"code":serviceCallResults["code"]}
        if response_key is not None:
            return True,serviceCallResults[response_key]
        else:
            return True,serviceCallResults
    @staticmethod
    def SaveDfInFile(df,extension=".csv",sheet=None,template_guid=None):
        df_as_json=df.to_json(orient='records')
        serviceCallStatus,serviceCallResults= ServiceController.CallEurekaService(Services.FILE_SERVICE_NAME,Services.SAVE_DF_DATA_IN_FILE,data={"json_data":df_as_json,"extension":extension,"sheet":sheet,"template_guid":template_guid},response_key=Services.FILE_KEY)
        if not serviceCallStatus:
                return False,{'message':serviceCallResults["message"],"code":422}
        outfilename=serviceCallStatus
        return True,outfilename


    @staticmethod
    def ReturnErrorMessage(error_message=None):
            return HttpResponse(json.dumps({'status': False, 'message': error_message["message"]}),status=error_message["code"],
                                        content_type='application/json')



    # def CloseConnection():
    #     print("eureka call to ",service_url)
    #     # self._service_tag=service_url
    #     serviceCallResults= json.loads(eureka_client.do_service(self._service_name,service_url,data=data,method=request_type))
    #     if serviceCallResults["status"] == False:
    #             self._response_error={'message':serviceCallResults["message"],"code":serviceCallResults["code"]}
    #             return False
    #     if response_key is not None:
    #         self._response_data=serviceCallResults[response_key]
    #     else:
    #         self._response_data=serviceCallResults
    #     return True


