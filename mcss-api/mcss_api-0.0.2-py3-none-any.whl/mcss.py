import requests
from requests.auth import HTTPBasicAuth
import json

def convertServer(serverJson, mcss):
    tmp_server = server(mcss)
    tmp_server.guid = serverJson["guid"]
    tmp_server.status = serverJson["status"]
    tmp_server.name = serverJson["name"]
    tmp_server.description = serverJson["description"]
    tmp_server.pathToFolder = serverJson["pathToFolder"]
    tmp_server.folderName = serverJson["folderName"]
    tmp_server.creationDate = serverJson["creationDate"]
    tmp_server.isSetToAutoStart = serverJson["isSetToAutoStart"]
    tmp_server.keepOnline = serverJson["keepOnline"]
    tmp_server.javaAllocatedMemory = serverJson["javaAllocatedMemory"]
    tmp_server.javaStartupLine = serverJson["javaStartupLine"]
    return tmp_server

def sendRequest(method, url, data, headers, token):
    if headers is None:
        headers = {'APIKey': token}
    else:
        headers['APIKey'] = token
    if method == "GET":
        response = requests.get(url, json=data, headers=headers)
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)
    return response


class MCSS():
    online = 1

    con_open = False
    host = None

    def __init__(self, host, quit) -> None:
        try:
            r = sendRequest("GET", host + "/", None, None, None)
        except:
            if quit == True:
                raise Exception("Invalid host")
            else:
                print("Invalid host")
                return None
        if r.status_code != 200:
            if quit == True:
                raise Exception("Invalid host")
            else:
                print("Invalid host")
                return None
        
        self.con_open = True
        self.host = host

    # def auth(self, username, password) -> None:
    #     url = self.host + "/api/token"
    #     data = {
    #         "username": username,
    #         "password": password
    #     }
    #     r = requests.post(url, data=data)
    #     if r.status_code != 200:
    #         raise Exception("Authentication failed")
    #     return r.json()["access_token"]

    def getServers(self, token):
        url = self.host + "/api/v1/servers"
        # r = requests.get(url, headers={"Authorization": "Bearer " + token})
        r = sendRequest("GET", url, None, None, token)
        if r.status_code != 200:
            raise Exception("Failed to get servers")

        servers = []
        for server in r.json():
            servers.append(convertServer(server, self))
        return servers

    def getServer(self, token, guid): 
        url = self.host + "/api/v1/server/" + guid
        r = sendRequest("GET", url, None, None, token)
        if r.status_code != 200:
            raise Exception("Failed to get server")
        return convertServer(r.json(), self)

    def serverCount(self, token):
        url = self.host + "/api/v1/servers/count"
        r = sendRequest("GET", url, None, None, token)
        if r.status_code != 200:
            raise Exception("Failed to get server count")
        return int(r.content.decode("utf-8"))

    def onlineServerCount(self, token):
        url = self.mcss_instance.host + "/api/v1/servers/count/online"
        r = sendRequest("GET", url, None, None, token)
        if r.status_code != 200:
            raise Exception("Failed to get online server count")
        return int(r.content.decode("utf-8"))
    def serverCountOnline(self, token):
        return self.onlineServerCount(token)

class server():
    mcss_instance = None

    def __init__(self, mcss) -> None:
        self.mcss_instance = mcss

    guid = None
    status = 0
    name = None
    description = None
    pathToFolder = None
    folderName = None
    creationDate = None
    isSetToAutoStart = False
    keepOnline = 0
    javaAllocatedMemory = None
    javaStartupLine = None
    statistic = None
    
    def getStatus(self):
        r = sendRequest("GET", self.mcss_instance.host + "/api/v1/servers/" + self.guid + "?filter=Status", None, None, None)
        if r.status_code != 200:
            raise Exception("Failed to get status")
        self.status = r.json()["status"]
        switch = {
            0: "Offline",
            1: "Online",
            2: "Unknown",
            3: "Starting",
            4: "Stopping"
        }
        return switch.get(self.status, "Unknown")

    #
    # Server Actions
    #
    def action(self, action, token):
        url = self.mcss_instance.host + "/api/v1/servers/"+ self.guid +"/execute/action"
        # r = requests.post(url, headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"}, json={"Guid": self.guid, "Action": action})
        r = sendRequest("POST", url, {"action": action}, None, token)
        if r.status_code != 200:
            raise Exception("Failed to " + action)

    def start(self, token):
        self.action("1", token)

    def stop(self, token):
        self.action("2", token)

    def restart(self, token):
        self.action("3", token)

    def kill(self, token):
        self.action("4", token)

    def command(self, command, token):
        url = self.mcss_instance.host + "/api/server/execute/command"
        r = requests.post(url, headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"}, json={"Command": command, "Guid": self.guid})
        if r.status_code != 200:
            raise Exception("Failed to execute command")
    def runCommand(self, command, token):
        self.command(command, token)
    def sendCommand(self, command, token):
        self.command(command, token)
    def massCommand(self, commands, token):
        for command in commands:
            self.command(command, token)
    def commands(self, commands, token):
        self.massCommand(commands, token)
    def sendCommands(self, commands, token):
        self.massCommand(commands, token)


    #
    # Console
    #
    def getConsole(self, guid, lines, reversed, token):
        url = self.mcss_instance.host + "/api/server/console"
        r = requests.get(url, headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"}, json={"Guid": guid, "AmountOfLines": lines, "Reversed": reversed})
        if r.status_code != 200:
            raise Exception("Failed to get console")
        return r.json()

    def console(self, lines, reversed, token):
        return self.getConsole(self.guid, lines, reversed, token)

    def getConsoleOutdated(self, secondLastLine, lastLine, token):
        url = self.mcss_instance.host + "/api/server/console/outdated"
        r = requests.get(url, headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"}, json={"Guid": self.guid, "SecondLastLine": secondLastLine, "LastLine": lastLine})
        if r.status_code != 200:
            raise Exception("Failed to get console outdated")
        if r.content.decode("utf-8") == "true":
            return True
        else:
            return False

    
