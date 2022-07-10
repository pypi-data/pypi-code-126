    
import json
from typing import Tuple

from django.http import HttpRequest

#from TDhelper.generic.dictHelper import findInDict

class Request:
    META={}
    query_params={}
    data={}
    file={}

class Response:
    data={}

def findInDict(findKey, source: 'dict|type'):
    '''
        根据finkey查找dict.
        - Params:
        -   findkey: <str>, formatter("node1.node2.node3").
        -   source: <dict>, it is your search target, findkey must in it. if findkey not in it, then raise an error
        - Returns: <any>, if can't found, then return None.
    '''
    result = None
    search_node = ''
    for key in findKey.split('.'):
        search_node += ("." if search_node else "") + key
        if isinstance(source,dict):
            if key not in source:
                raise Exception("can not found key(%s)" % search_node)
            result = source[key]
            source = source[key]
        elif isinstance(source,object):
            result= getattr(source,key)
            if not result:
                raise Exception("can not found key(%s)" % search_node)
            else:
                source= result
    return result


def set_params_mapping(back_ret: dict, isLocation:bool, key:str, relation:dict, *args, **kwargs):
        """
        set trigger func params mapping to handle's params.
        """
        if "key" in relation:
            if relation["key"]:
                m_key = relation["key"].split(".")
            else:
                m_key = None
        else:
            m_key = None
        if "sources" in relation:
            sources = relation["sources"]
        else:
            sources = None
        if not m_key:
            if "default" not in relation:
                value = None
            else:
                value = relation["default"]
        else:
            if not sources:
                if len(m_key) >= 2:
                    if m_key[0].lower() == "args":
                        if len(m_key)!=2:
                            if "default" not in relation:
                                value= None
                            else:
                                value= relation["default"]
                        else:
                            if int(m_key[1]) < len(args):
                                value = args[int(m_key[1])]
                            else:
                                if "default" not in relation:
                                    value = None
                                else:
                                    value = relation["default"]
                    elif m_key[0].lower() == "kwargs":
                        try:
                            find_key=relation["key"].lstrip(r"kwargs").lstrip('.')
                            value = findInDict(find_key, kwargs)
                        except Exception as e:
                            if "default" not in relation:
                                print(e.args)
                                value = None
                            else:
                                value = relation["default"]
                    elif m_key[0].lower() == "request":
                        m_context = None
                        for o in args:
                            if isinstance(o, Request):
                                m_context = o
                                break
                        if m_context:
                            try:
                                find_key=relation["key"].lstrip('request').lstrip('.')
                                value = findInDict(find_key, m_context)
                            except Exception as e:
                                if "default" not in relation:
                                    print(e.args)
                                    value = None
                                else:
                                    value = relation["default"]
                        else:
                            if "default" not in relation:
                                print("not found context 'request'.")
                                value = None
                            else:
                                value = relation["default"]
                    else:
                        if "default" not in relation:
                            value = None
                        else:
                            value = relation["default"]
                else:
                    if "default" not in relation:
                        value = None
                    else:
                        value = relation["default"]
                if isLocation:
                    mapping_key= key.split('.')
                    if len(mapping_key)==2:
                        if mapping_key[0].lower()=="args":
                            if int((mapping_key[1])) < len(back_ret["args"]):
                                back_ret["args"].insert(int(mapping_key[1]),value)
                            else:
                                back_ret["args"].append(value)
                        elif mapping_key[0].lower()=="kwargs":
                            back_ret["kwargs"][mapping_key[1]] = value
                        else:
                            if int((mapping_key[1])) < len(back_ret["args"]):
                                back_ret["args"].insert(int(mapping_key[1]),value)
                            else:
                                back_ret["args"].append(value)
                    else:
                        back_ret["args"].append(value)
                else:
                    back_ret[key] = value
            else:
                if "master_func_results" in kwargs:
                    m_func_result = kwargs["master_func_results"]
                    relation_key= key.lstrip('self').lstrip('.')
                    if isinstance(m_func_result, Response):
                        m_func_result = m_func_result.data
                    if isinstance(m_func_result, (tuple, list)):
                        # master func results is Indexes type, mapping process
                        if key == "self":
                            value = m_func_result
                        else:
                            result_key = key.split(".")
                            if len(result_key) == 2:
                                if int(result_key[1]) < len(m_func_result):
                                    value = m_func_result[int(result_key[1])]
                                else:
                                    value = None
                            else:
                                value = None
                    elif isinstance(m_func_result, (dict,)):
                        if key == "self":
                            value = m_func_result
                        else:
                            try:
                                value = findInDict(relation_key, m_func_result)
                            except Exception as e:
                                if "default" not in relation:
                                    print(e.args)
                                    value = None
                                else:
                                    value = relation["default"]
                    else:
                        # master func results is object
                        if key == "self":
                            value = m_func_result
                        else:
                            try:
                                value = findInDict(relation_key, m_func_result)
                            except Exception as e:
                                if "default" not in relation:
                                    print(e.args)
                                    value = None
                                else:
                                    value = relation["default"]
                    # mapping params
                    if isLocation:
                        if len(m_key) == 2:
                            if m_key[0].lower() == "args":
                                if int(m_key[1]) < len(back_ret["args"]):
                                    back_ret["args"].insert(int(m_key[1]),value)
                                else:
                                    back_ret["args"].append(value)
                            else:
                                back_ret["kwargs"][m_key[1]] = value
                        else:
                            back_ret["kwargs"][m_key] = value
                    else:
                        back_ret[m_key[1]] = value
        return back_ret

def generic_params(mapping: 'dict|str', isLocation:bool=False, *args, **kwargs):
        """
        generic create params.
        - Params:
        -   mapping:<json>, params relation mapping.
        -   isLocation:<bool>, is location call, defalut(false).
        -   *args: <tuple>, original params.
        -   **kwargs: <dict>, original params.
        """
        ret = {}
        if isLocation:
            ret = {"args": [], "kwargs": {}}
        if isinstance(mapping,str):
            try:
                mapping = json.loads(mapping, encoding="utf-8")
            except Exception as e:
                print(e)
                mapping = {}
        for k, v in mapping.items():
            set_params_mapping(ret, isLocation, k, v, *args, **kwargs)
        if isLocation:
            ret['args']= tuple(ret['args'])
        return ret

import __init__
import unittest
import datetime
from TDhelper.document.excel.model import model
from TDhelper.document.excel.FieldType import FieldType

request= Request()

request.META["HTTP_API_TOKEN"]="HTTP_API_TOKEN"
request.query_params={
    "query1":"query1",
    "query2":"query2",
    "query3":"query3"
}
request.data={
    "data1":"data1",
    "data2":"data2",
    "data3":"date3"
}


response= Response()
response.data={
    "state":True,
    "data":{
        "res_key1":"res_key1",
        "res_key2":{
            "res_key3":{
                "res_key4":"res_key4"
            }
        }
    }
}
class testReturnObj:
    res_key1= "res_key1"
    res_key2={
            "res_key3":{
                "res_key4":"res_key4"
            }
        }
testReturnTuple=("res_1","res_2")
args=(request,2,3,4,5,)
kwargs={
    "key1":"key1",
    "key2":"key2",
    "key3":"key3",
    "key4":{
        "key5":{
            "key6":"key6"
        }
    },
    "master_func_results":testReturnTuple
}

config={
    "args.0": {
		"key": "args.0",
		"default": "0"
	},
    "args.1": {
        "key": "args.1",
        "default": "0"
    },
	"kwargs.get_kwargs1":{
		"key":"kwargs.key1",
		"default":"0"
	},
	"args.3":{
		"key":"request.META.HTTP_API_TOKEN"
	},
    "kwargs.get_args_set_kwargs3":{
        "key":"args.2"
    },
    "kwargs.get_layer_kwargs_set_kwargs":{
        "key":"kwargs.key4.key5.key6"
    },
    "self":{
        "key":"kwargs.get_func_ret_set_kwargs",
        "sources":True
    },
    "self.0":{
        "key":"args.2",
        "sources":True
    },
    "self.1":{
        "key":"kwargs.get_res_set_kwargs_res_key4",
        "sources":True
    },
}
class TestDoumentExcel(unittest.TestCase):
    def test_genernal_param(self):
        sss=generic_params(config,False,*args,**kwargs)
        print(sss)
if __name__ == "__main__":
    unittest.main()