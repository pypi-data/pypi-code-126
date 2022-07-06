import requests
import json
import distutils.util as util


def deserialize(message, outputType): # deserialize function to transform responses into string, boolean or json dictionaries
    desMessage = None

    if message.ok:
        if outputType == 'string':
            desMessage = message.text.replace('"', '')

        elif outputType == 'boolean':
            desMessage = bool(util.strtobool(message.text))

        elif outputType == 'json':
            desMessage = json.loads(message.content)

    return desMessage


def apiConnection(*args): # manage api calls
    if len(args) == 2: # echoping
        response = deserialize(requests.get(args[0]), args[1])
    
    elif len(args) == 3: # normal get calls
        response = deserialize(requests.get(args[0], headers=args[1]), args[2])
    
    elif len(args) == 4: # create context
        response = deserialize(requests.post(args[0], data=args[1]), args[2])
    
    elif len(args) == 5: # post asset
        args[1].update({'Content-Type': 'application/json'})

        response = deserialize(requests.post(args[0], headers=args[1], data=args[2]), args[3])
    
    return response