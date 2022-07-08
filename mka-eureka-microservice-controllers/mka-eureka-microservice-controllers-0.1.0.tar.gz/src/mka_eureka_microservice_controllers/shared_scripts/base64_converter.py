import base64
import pickle

class Base64Converter(object):
    

    @classmethod
    def B64ToPickle(b64_pickle):
        pickleData=base64.b64decode(b64_pickle)
        pickleData=pickle.loads(pickleData)
        return pickleData
    @classmethod
    def PickleToB64(pickle_data):
        b64Pickle=pickle.dumps(pickle_data)
        b64Pickle=f"""{base64.b64encode(b64Pickle).decode()}"""
        return b64Pickle
    @classmethod
    def B64ToHtml(b64_html):
        html_str=base64.b64decode(b64_html)
        return html_str
    @classmethod
    def HtmlToB64(html_str):
        b64_html=base64.b64encode(html_str.encode('ascii')).decode()
        return b64_html

    # def FileUploadToB64(html_str):
    #     b64_html=base64.b64encode(html_str.encode('ascii')).decode()
    #     return b64_html

