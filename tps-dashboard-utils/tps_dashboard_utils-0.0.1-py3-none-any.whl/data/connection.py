import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

# Get the server and db from environmental variables
load_dotenv()
DRIVER = '{SQL Server}'
SERVER = os.environ.get('SERVER')
DATABASE = os.environ.get('DATABASE')

# Create the connection string
connection_string = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};trusted_connection='yes';autocommit=True"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
