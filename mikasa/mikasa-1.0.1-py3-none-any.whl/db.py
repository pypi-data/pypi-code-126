import sqlite3
import os
from termcolor import colored as log


db_name = os.path.abspath(os.getcwd())+"\\config.sqlite3"

def draw():
    db = sqlite3.connect(db_name)
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
    
def insert(name:str,path:str):
    
    if not os.path.exists(path):
        print("path not found ")
        exit()

    
    db = sqlite3.connect(db_name)
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

def fetch(name):
    db = sqlite3.connect(db_name)
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


def delete(name):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    
    QUERY = f""" DELETE FROM projects where name = '{name}' """
    

    try:
        cursor.execute(QUERY)
        print(f"{name} was deleted ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()