# -*- coding:utf-8 -*-
import os
import sys
import requests
import json

automation_api_root_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../'))

if  automation_api_root_path not in sys.path:
    sys.path.insert(0, automation_api_root_path)

from swagger_client.configuration import Configuration

layer_endpoint = "/layer"
layers_endpoint = "/layers"

#graphics_url = "http://localhost:8000/arcgisearth/graphics"


from api_wrapper.api_wrapper import BasicAPIWrapper

class HttpAPIWrapper(BasicAPIWrapper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graphics_url = self.base_url + "/arcgisearth/graphics"
        self.base_address = self.base_url + "/arcgisearth"
        self.api_version_str = "?api-version={}".format(self.version)
    
    
    def get_camera(self):
        url = self.base_address + "/camera" 
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def set_camera(self, camera):
        url = self.base_address + "/camera" 
        headers = {"content-Type": "application/json"}

        r = requests.put(url, data=json.dumps(camera), headers=headers, verify=False)
        return r.status_code, r.json()

    def set_flight(self, flight):
        url = self.base_address + "/flight"
        headers = {"content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(flight), headers=headers, verify=False)
        return r.status_code, r.json()

    def add_layer(self, layer):
        url = self.base_address + layer_endpoint +  self.api_version_str
        headers = {"content-Type": "application/json"}

        r = requests.post(url, data=json.dumps(layer),
                            headers=headers, verify=False)
        return r.status_code, r.json()

    def get_layer(self, layer_id):
        url = self.base_address + layer_endpoint + "/" + layer_id + self.api_version_str
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def remove_layer(self, layer_id):
        url = self.base_address + "/layer/" + layer_id
        r = requests.delete(url)
        return r.status_code, r.json()

    def clear_layers(self, target="operationallayers"):
        url = self.base_address + layers_endpoint + "/" + target + self.api_version_str
        r = requests.delete(url, verify=False)
        return r.status_code, r.json()

    def add_graphic(self, graphic):
        headers={'content-Type': 'application/json'}
        graphic_json_str = json.dumps(graphic)
        response = requests.post(self.graphics_url, data=graphic_json_str, headers=headers,verify=False)
        return response.status_code, response.json()

    def get_graphic(self, graphic_id):
        url = self.base_address + "/graphics/" + graphic_id
        r = requests.get(url, verify=False)
        return r.status_code, r.json()


    def update_graphic(self, graphic):
        url = self.base_address + "/graphics" 
        headers = {"content-Type": "application/json"}
        r = requests.patch(url, data=json.dumps(graphic), headers=headers, verify=False)
        return r.status_code, {}

    def remove_graphic(self, graphic_id):
        url = self.base_address + "/graphics/" + graphic_id
        r = requests.delete(url)
        return r.status_code, {} 

    def clear_graphics(self):
        url = self.base_address + "/graphics"
        r = requests.delete(url)
        return r.status_code, {} 

    def add_drawing(self, drawing):
        url = self.base_address + "/drawings/"
        headers={'content-Type': 'application/json'}
        drawing_json_str = json.dumps(drawing)
        response = requests.post(url, data=drawing_json_str, headers=headers,verify=False)
        return response.status_code, response.json()

    def remove_drawing(self, drawing_id):
        url = self.base_address + "/drawings/" + drawing_id
        r = requests.delete(url)
        return r.status_code, {}

    def clear_drawings(self):
        url = self.base_address + "/drawings/"
        r = requests.delete(url)
        return r.status_code, {} 

    def get_workspace(self):
        url = self.base_address + "/workspace"
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def import_workspace(self, workspace_info):
        url = self.base_address + "/workspace"
        headers = {"content-Type": "application/json"}
        data = json.dumps(workspace_info)
        r = requests.put(url, data=data, stream=True)
        return r.status_code, r.json()

    def clear_workspace(self):
        url = self.base_address + "/workspace"
        r = requests.delete(url)
        return r.status_code, r.json()

    def get_snapshot(self):
        url = self.base_address + "/snapshot/"
        r = requests.get(url)
        return r.status_code, r