import pymysql
import pymysql.cursors


class Mysql:
    def __init__(self, host, username, password, database):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.con = None

    def connect(self):
        try:
            self.con = pymysql.connect(host=self.host,
                                       user=self.username,
                                       password=self.password,
                                       database=self.database,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError:
            return False
        return True

    def getcon(self):
        return self.con

    def query(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        r = cur.fetchall()
        cur.close()
        return r

    def updatequery(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        r = cur.fetchall()
        self.con.commit()
        cur.close()
        return r
