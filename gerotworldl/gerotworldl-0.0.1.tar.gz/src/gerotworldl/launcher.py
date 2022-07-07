from .import *


class Launcher:
    def __init__(self, version, connection, mysql):
        self.version = version
        self.connection = connection
        self.mysql = mysql

    def isupdates(self):
        if self.version != self.connection.getserverdata()["version"]:
            return True
        return False

    def auth(self, username, password):
        query = f'SELECT * FROM users WHERE `nickname`="{username}"'
        user = self.connection.getauthuser(query, self.mysql)
        if not user:
            return ""
        password_verify = customrequest(self.connection.getmainurl() + f"scripts/verifyhash.php?string={password}&hash={user[0]['password']}")
        if password_verify != b"1":
            return ""
        return "OK:" + user[0]["nickname"], user

    def getconnection(self):
        return self.connection

    def getmysql(self):
        return self.mysql

