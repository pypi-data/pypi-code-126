from email.policy import default
from importlib.resources import path
from lib2to3.pgen2.token import LEFTSHIFT
import sqlite3
import os
from termcolor import colored as log
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

CONFIG_DB = os.path.join(BASE_DIR,'config.sqlite3')


def handle_data_db():
    db = sqlite3.connect(CONFIG_DB)
    cursor = db.cursor()
    
    QUERY = """CREATE TABLE IF NOT EXISTS config ( db text NOT NULL PRIMARY KEY , path text NOT NULL  )"""
    
    
    try:
        cursor.execute(QUERY)
        print("create config tables done ".capitalize())

    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")
    db.commit()

handle_data_db()

def db_path(db_name="default"):
    db = sqlite3.connect(CONFIG_DB)
    cursor = db.cursor()
    QUERY = f"SELECT * FROM config WHERE db = '{db_name}'"
    result = cursor.execute(QUERY)
    db.commit()
    result = result.fetchall()
    if not result:
        print(" you have not choice any db config yet  ".capitalize())
        name = input("insert database name [default is 'default' ]  ").replace(" ","_")
        if name : db_name = name
        path = input("database path ? :  ".capitalize())
        QUERY = f"INSERT INTO config (db,path) VALUES ('{db_name}','{path}') "
        res = cursor.execute(QUERY)
        db.commit()
        
        db_path()
        exit()

    db.commit()
    
    res = result[0][1]
    
    if res.endswith("\\"):
        res = res+db_name+".sqlite3"
    elif res.endswith("/"):
        res = res.replace("/","\\")
        res = res+db_name+".sqlite3"
    else:
        res = res+"{db_name}\\.sqlite3"
    db.commit()
    return res

db_path()








DBPATH = db_path()

def change_db(dbname):
    
    
    db = sqlite3.connect(CONFIG_DB)
    cursor = db.cursor()
    QUERY = f"SELECT * from config WHERE db='{dbname}' "
    query = cursor.execute(QUERY)
    result = query.fetchall()
    
    
    
    if not result:
        print(f"you do not have any database match the name {dbname} \n you have to insert new database to match this name ")

        name = input("database name  ".capitalize())
        path = input("database path  ".capitalize())

        if name : dbname = name
        
        QUERY = f"INSERT INTO config (db,path) VALUES ('{name}','{path}')  "
        
        cursor.execute(QUERY)
        
        db.commit()
        
        QUERY = f"SELECT path FROM config where db='{name}' "
        
        result = cursor.execute(QUERY).fetchall()

    global DBPATH
    
    DBPATH = result[0][1] 
    
    if str(DBPATH).endswith("\\"):
        DBPATH = DBPATH + f"{result[0][0]}.sqlite3"
    
    elif str(DBPATH).endswith("/"):
        DBPATH = DBPATH.replace("/","\\")
        DBPATH = DBPATH + f"{result[0][0]}.sqlite3"
    
    else:
        DBPATH = DBPATH.replace("/","\\")
        DBPATH = DBPATH + f"\\{result[0][0]}.sqlite3"
    
    print(f"you fetch database has been changed not its in {result[0][1]} ")
    exit()






def drop(db=DBPATH):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    
    QUERY = """
        DROP TABLE IF EXISTS projects
    """
    
    try:
        cursor.execute(QUERY)
        print("droping tables done ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")
    db.commit()

def draw(db=DBPATH):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    
    QUERY = """
    
    CREATE TABLE IF NOT EXISTS projects ( name text NOT NULL PRIMARY KEY , path text NOT NULL  )
    
    """
    
    try:
        cursor.execute(QUERY)
        print("handling tables done ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()
    
def insert_data(name:str,path:str,db=DBPATH):
    
    if not os.path.exists(path):
        print("path not found ")
        exit()

    
    db = sqlite3.connect(db)
    cursor = db.cursor()
    QUERY = f'''
    
    INSERT INTO projects (name,path) VALUES ('{name}','{path}')
    
    '''
    try:
        cursor.execute(QUERY)
        print("insert data done ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()

def update_data(name,path,db=DBPATH):
    if not os.path.exists(path):
        print("path not found ")
        exit()

    
    db = sqlite3.connect(db)
    cursor = db.cursor()
    QUERY = f'''
    
    UPDATE projects SET path = '{path}' WHERE name = '{name}'
    
    '''
    try:
        cursor.execute(QUERY)
        print("update data done ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()


def fetch(name,db=DBPATH):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    QUERY = f''' SELECT * FROM projects  WHERE name = '{name}' '''
    try:
        res = cursor.execute(QUERY)
        try:
            result = res.fetchall()[0][1]
            return result
        except IndexError:
            print("project not found")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()
    
    return None


def delete(name,db=DBPATH):
    db = sqlite3.connect(db)
    cursor = db.cursor()
    
    QUERY = f""" DELETE FROM projects where name = '{name}' """
    

    try:
        cursor.execute(QUERY)
        print(f"{name} was deleted ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()