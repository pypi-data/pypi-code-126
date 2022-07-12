import json
import os
import requests

def visit_digolds():
    current_file_dir = os.path.dirname(__file__)
    f = open(os.path.join(current_file_dir,'host.json'))
    domain = json.load(f).get('domain')
    html = requests.get(domain)
    return html
    