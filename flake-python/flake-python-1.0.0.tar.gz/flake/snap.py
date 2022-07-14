from watchpoints import watch as snap, watch_element
from .shared import output
from .time import getTime

output["scope"] = {}

def registerVariableChange(frame: watch_element.WatchElement, elem, info):
	line = info[2]
	value = elem.obj
	name = elem.localvar
	output["scope"][name] = value
	output["snapshots"].append({
		"time": getTime(),
		"event": {
			"type": "reassign",
			"line": line - 1,
			"name": name,
			"value": value
		},
		"context": {},
		"scope": output["scope"]
	})

snap.config(custom_printer=lambda x: x, callback=registerVariableChange)