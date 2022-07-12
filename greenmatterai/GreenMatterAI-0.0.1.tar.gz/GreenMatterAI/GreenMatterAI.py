import requests
import json
import boto3
import os
from aws_requests_auth.aws_auth import AWSRequestsAuth


class GMAI:
    def __init__(self, task, access_key_id, secret_access_key):
        self._bucket = 'gmai-test-bucket'
        self._region = 'eu-central-1'
        self._api_service = 'execute-api'

        if task == 'test':
            self._url = 'https://mgedkusjqb.execute-api.eu-central-1.amazonaws.com/test/test_lambda'
            self._api_host = 'mgedkusjqb.execute-api.eu-central-1.amazonaws.com'
            self._folder = 'test'
        elif task == 'yolov3-synthetic':
            self._url = 'https://v3ljyf1pif.execute-api.eu-central-1.amazonaws.com/test/yolo'
            self._api_host = 'v3ljyf1pif.execute-api.eu-central-1.amazonaws.com'
            self._folder = 'synthetic'
        elif task == 'yolov3-real':
            self._url = 'https://v3ljyf1pif.execute-api.eu-central-1.amazonaws.com/test/yolov3-real'
            self._api_host = 'v3ljyf1pif.execute-api.eu-central-1.amazonaws.com'
            self._folder = 'real'
        else:
            self._url = None
            self._api_host = None
            self._folder = None

        self._auth = AWSRequestsAuth(aws_access_key=access_key_id,
                                     aws_secret_access_key=secret_access_key,
                                     aws_host=self._api_host,
                                     aws_region=self._region,
                                     aws_service=self._api_service)
        self._s3_client = boto3.client('s3', region_name=self._region, aws_access_key_id=access_key_id,
                                       aws_secret_access_key=secret_access_key)

    def query(self, image_path):
        folder_path, file_name = os.path.split(image_path)
        s3_path = self._folder + '/data/' + file_name
        self._s3_client.upload_file(image_path, self._bucket, s3_path)

        test_dict = {"image_path": s3_path, "file_name": file_name, "bucket": self._bucket}

        response = requests.post(self._url, auth=self._auth, json=json.dumps(test_dict))

        if folder_path == "":
            output_file_name = "output.jpg"
        else:
            output_file_name = "\\output.jpg"
        output_file_path = folder_path + output_file_name
        self._s3_client.download_file(self._bucket, json.loads(response.text)["s3_path"], output_file_path)

        return output_file_path
