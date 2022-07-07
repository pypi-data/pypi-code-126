import datetime


class Session:
    def __init__(self, uuid, mysql, dt, days):
        self.uuid = uuid
        self.mysql = mysql
        self.dt = dt
        self.username = None
        self.days = days

    def isactive(self):
        user = self.mysql.query(f'SELECT * FROM `users` WHERE uuid="{self.uuid}"')
        if not user:
            return False
        tm = user[0]['lsessiontm']
        self.username = user[0]['nickname']
        if tm != 0:
            if int(tm) >= int(self.dt.now().timestamp()):
                return True
        return False

    def create(self):
        self.uuid = self.readuuid()
        user = self.mysql.query(f'SELECT * FROM `users` WHERE uuid="{self.uuid}"')
        now = datetime.datetime.now()
        increase = datetime.timedelta(days=self.days)
        timestamp = str(int((now + increase).timestamp()))
        self.mysql.updatequery(f'UPDATE `users` SET lsessiontm="{timestamp}" WHERE nickname="{user[0]["nickname"]}"')

    def writeuuid(self, user):
        with(open("session.txt", "w") as file):
            file.write(user[0]['uuid'])

    def readuuid(self):
        with(open("session.txt", "r") as file):
            return file.read()

    def destroy(self):
        user = self.mysql.query(f'SELECT * FROM `users` WHERE uuid="{self.uuid}"')
        self.mysql.updatequery(f'UPDATE `users` SET lsessiontm="0" WHERE nickname="{user[0]["nickname"]}"')
        with(open("session.txt", "w") as file):
            file.write("nouuid")

    def getusername(self):
        return self.username
