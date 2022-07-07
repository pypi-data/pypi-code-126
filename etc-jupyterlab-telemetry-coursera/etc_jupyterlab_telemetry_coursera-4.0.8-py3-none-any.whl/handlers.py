from requests import Session, Request
from ._version import _fetchVersion
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin
import os, json, concurrent, tornado
import urllib.request
import re
import pathlib

class RouteHandler(ExtensionHandlerMixin, JupyterHandler):

    executor = concurrent.futures.ThreadPoolExecutor(5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.etc_bucket_url = None
        self.etc_telemetry = self.extensionapp.etc_telemetry
    
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self, resource):
   
        try:
            self.set_header('Content-Type', 'application/json')

            if resource == 'workspace_id':
                workspace_id = os.getenv('WORKSPACE_ID') if os.getenv('WORKSPACE_ID') is not None else 'UNDEFINED'
                self.finish(json.dumps(workspace_id))

            elif resource == 'telemetry':
                url = self.extensionapp.etc_url
                bucket = self.extensionapp.etc_bucket
                path = self.extensionapp.etc_path
                env_path_segment_names = self.extensionapp.etc_env_path_segment_names

                 #
                parts = [part for part in [
                    url, bucket, path] if part]
                self.etc_bucket_url = '/'.join(parts)
                #  Construct the bucket_url from the url, bucket, and path.

                #
                for env_path_segment_name in env_path_segment_names:
                    env_path_segment_value = os.getenv(env_path_segment_name, None)
                    if env_path_segment_value:
                        self.etc_bucket_url = f'{self.etc_bucket_url}/{env_path_segment_value}'
                #  Append the values of specified environment variables to the bucket_url.

                if self.extensionapp.etc_telemetry_path and self.etc_telemetry is None:
                    telemetry_file_path = pathlib.Path(self.extensionapp.etc_telemetry_path, '.telemetry')
                    #  If telemetry isn't configured look for the presence of the touch file in order to activate telemetry.
                    #  This is useful when telemetry should be activated by the presence of a file in the Lab home directory.
                    if telemetry_file_path.is_file():
                        self.etc_telemetry = True
                        with open(telemetry_file_path, 'r') as f:
                            segment = f.read().strip()
                            acs = '[a-z0-9-]'
                            regex = rf'^(?:{acs}|(?<={acs})/(?={acs}))+$'
                            if segment and re.search(regex, segment, flags=re.IGNORECASE):
                                self.etc_bucket_url = f'{self.etc_bucket_url}/{segment}'
                            #  If telemetry is on and if the touch file is present, read its contents and append it to the bucket_url.                        
                
                if self.etc_telemetry is None:
                    self.etc_telemetry = False

                self.finish(json.dumps({'telemetry' : self.etc_telemetry}))

            elif resource == 'config':
                self.finish(json.dumps(self.config))
            elif resource == 'environ':
                self.finish(json.dumps({k:v for k, v in os.environ.items()}))
            elif resource == 'version':
                self.finish(json.dumps(_fetchVersion()))
            else:
                self.set_status(404)

        except Exception as e:
            self.log.error(str(e))
            self.set_status(500)
            self.finish(json.dumps(str(e)))

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def post(self, resource):
        try:

            if resource == 's3' and self.etc_telemetry:

                result = yield self.process_request()

                self.finish(json.dumps(result))

            else:
                self.set_status(404)

        except Exception as e:
            self.log.error(str(e))
            self.set_status(500)
            self.finish(json.dumps(str(e)))

    @tornado.concurrent.run_on_executor 
    def process_request(self):
        
        try:
            data = self.request.body
            
            with Session() as s:

                req = Request(
                    'POST', 
                    self.etc_bucket_url, 
                    data=data, 
                    headers={
                        'Content-Type': 'application/json'
                        })

                prepped = s.prepare_request(req)

                res = s.send(prepped, proxies=urllib.request.getproxies())

                return {
                    'status_code': res.status_code,
                    'reason': res.reason,
                    'text': res.text
                }

        except Exception as e:
            self.log.error(str(e))