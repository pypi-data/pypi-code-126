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

base_address = Configuration().host + "/arcgisearth" 
api_version_1 = "?api-version=1.0"
api_version_latest = "?api-version=latest"
layer_endpoint = "/layer"
layers_endpoint = "/layers"

graphics_url = "http://localhost:8000/arcgisearth/graphics"


from api_wrapper.api_wrapper import BasicAPIWrapper

class HttpAPIWrapper(BasicAPIWrapper):

    def __init__(self, api_version="1.16"):
        super().__init__(api_version)
    
    
    def get_camera(self):
        url = base_address + "/camera" 
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def set_camera(self, camera):
        url = base_address + "/camera" 
        headers = {"content-Type": "application/json"}

        r = requests.put(url, data=json.dumps(camera), headers=headers, verify=False)
        return r.status_code, r.json()

    def set_flight(self, flight):
        url = base_address + "/flight"
        headers = {"content-Type": "application/json"}
        r = requests.post(url, data=json.dumps(flight), headers=headers, verify=False)
        return r.status_code, r.json()

    def add_layer(self, layer):
        url = base_address + layer_endpoint +  api_version_latest
        headers = {"content-Type": "application/json"}

        r = requests.post(url, data=json.dumps(layer),
                            headers=headers, verify=False)
        return r.status_code, r.json()

    def get_layer(self, layer_id):
        url = base_address + layer_endpoint + "/" + layer_id + api_version_latest
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def remove_layer(self, layer_id):
        url = base_address + "/layer/" + layer_id
        r = requests.delete(url)
        return r.status_code, r.json()

    def clear_layers(self, target="operationallayers"):
        url = base_address + layers_endpoint + "/" + target + api_version_latest
        r = requests.delete(url, verify=False)
        return r.status_code, r.json()

    def add_graphic(self, graphic):
        headers={'content-Type': 'application/json'}
        graphic_json_str = json.dumps(graphic)
        response = requests.post(graphics_url, data=graphic_json_str, headers=headers,verify=False)
        return response.status_code, response.json()

    def get_graphic(self, graphic_id):
        url = base_address + "/graphics/" + graphic_id
        r = requests.get(url, verify=False)
        return r.status_code, r.json()


    def update_graphic(self, graphic):
        url = base_address + "/graphics" 
        headers = {"content-Type": "application/json"}
        r = requests.patch(url, data=json.dumps(graphic), headers=headers, verify=False)
        return r.status_code, None

    def remove_graphic(self, graphic_id):
        url = base_address + "/graphics/" + graphic_id
        r = requests.delete(url)
        return r.status_code, None

    def clear_graphics(self):
        url = base_address + "/graphics"
        r = requests.delete(url)
        return r.status_code, None

    def add_drawing(self, drawing):
        url = base_address + "/drawings/"
        headers={'content-Type': 'application/json'}
        drawing_json_str = json.dumps(drawing)
        response = requests.post(url, data=drawing_json_str, headers=headers,verify=False)
        return response.status_code, response.json()

    def remove_drawing(self, drawing_id):
        url = base_address + "/drawings/" + drawing_id
        r = requests.delete(url)
        return r.status_code, r.json()

    def clear_drawings(self):
        url = base_address + "/drawings/"
        r = requests.delete(url)
        return r.status_code, None

    def get_workspace(self):
        url = base_address + "/workspace"
        r = requests.get(url, verify=False)
        return r.status_code, r.json()

    def import_workspace(self, workspace_info):
        url = base_address + "/workspace"
        headers = {"content-Type": "application/json"}
        data = json.dumps(workspace_info)
        r = requests.put(url, data=data, stream=True)
        return r.status_code, r.json()

    def clear_workspace(self):
        url = base_address + "/workspace"
        r = requests.delete(url)
        return r.status_code, r.json()

    def get_snapshot(self):
        url = base_address + "/snapshot/"
        r = requests.get(url)
        return r.status_code, r