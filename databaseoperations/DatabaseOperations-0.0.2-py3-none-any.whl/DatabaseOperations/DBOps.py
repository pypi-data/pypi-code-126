import pyodbc
import pandas as pd

class DBOps:
    def __init__(self, Server, Database, Username, Password):
        self.ConnectionString = "Driver={SQL Server Native Client 11.0};Server=" + Server + ";Database=" + Database + ";uid=" + Username +";pwd=" + Password

    def GetData(self, Query, Parameters = None):
        con = pyodbc.connect(self.ConnectionString)
        with con:
            df = pd.read_sql(Query, con)
            return df

    # def PostData(self, Query):