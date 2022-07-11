import fdb
import json
import datetime

def convertDateToIso8601(date):
    return date.strftime("%Y-%m-%dT%H:%M:%S.000")


def convertAllDatesInListDict(listDict):
    try:
        for dict in listDict:
            for key in dict:
                if isinstance(dict[key], datetime.datetime):
                    dict[key] = convertDateToIso8601(dict[key])
        return listDict
    except Exception as ex:
        print(ex)
        return listDict

class FirebirdConnect:
    def __init__(
                self, 
                host, 
                database, 
                lowerKeys=False,
                user='SYSDBA', 
                password='masterkey',
            ):
        self.database = database
        self.host = host
        self.lowerKeys = lowerKeys
        self.user = user
        self.password = password

    def connect(self):
        self.connection = fdb.connect(
            database=self.database,
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.connection.close()

    def select(self, query):
        try:
            self.connect()
            self.cursor.execute(query)
            r = []
            columns = [str(column[0]) for column in self.cursor.description]
            if self.lowerKeys:
                columns = [column.lower() for column in columns]
            for row in self.cursor.fetchall():
                r.append(dict(zip(columns, row)))
            r = convertAllDatesInListDict(r)
            resposta = json.dumps(r)
            self.disconnect()
            return resposta
        except Exception as ex:
            self.disconnect()
            erro = self.erro(query, ex, "select")
            return erro

    def execute(self, queries):
        try:
            self.connect()
            resposta = {"status": 200}
            for exec in queries:
                self.cursor.execute(exec)
            resposta = json.dumps(resposta)
            self.connection.commit()
            self.cursor.connection.close()
            return resposta
        except Exception as ex:
            self.cursor.connection.close()
            erro = self.erro(queries, ex, "execute")
            return erro

    def erro(self, value, erro, tipo):
        resposta = {"status": 500}
        resposta["erro"] = erro
        resposta["value"] = value
        resposta["tipo"] = tipo
        return json.dumps(resposta)
