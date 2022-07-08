import os
from .file_io import FileIO
from .get_arguments import get_argument
from datetime import datetime
import requests

class Http:
    def __init__(self) -> None:
        pass

    def download(self, remote_path, local_path, overwrite=True):
        get_response = requests.get(remote_path,stream=True)
        
        #original_file_name  = remote_path.split("/")[-1] # original name of the file. Ignored for now, but leave this for future needs
 
        with open(local_path, 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    
    def upload(self, local_path, remote_path, overwrite=True):
        raise NotImplementedError

    def get_modification_time(self):
        return datetime.now()
