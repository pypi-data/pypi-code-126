import sqlite3
import os
from termcolor import colored as log
from configparser import ConfigParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = os.path.join(BASE_DIR,'config.ini')
DBNAME = "base.sqlite3"

config = ConfigParser()
config.read(CONFIG_FILE)




def drop():
    db = sqlite3.connect(config.get("config","db"))
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

def draw():
    db = sqlite3.connect(config.get("config","db"))
    cursor = db.cursor()
    
    QUERY = """
    
    CREATE TABLE IF NOT EXISTS projects ( name text NOT NULL PRIMARY KEY , path text NOT NULL  )
    
    """
    
    try:
        cursor.execute(QUERY)
        print("handling tables done \n")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] \n ")

    db.commit()
    
def insert_data(name:str,path:str):
    
    if not os.path.exists(path):
        print("path not found ")
        exit()

    
    db = sqlite3.connect(config.get("config","db"))
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

def update_data(name,path):
    if not os.path.exists(path):
        print("path not found ")
        exit()

    
    db = sqlite3.connect(config.get("config","db"))
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


def fetch(name):
    db = sqlite3.connect(config.get("config","db"))
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
    db = sqlite3.connect(config.get("config","db"))
    cursor = db.cursor()
    
    QUERY = f""" DELETE FROM projects where name = '{name}' """
    

    try:
        cursor.execute(QUERY)
        print(f"{name} was deleted ")
    except Exception as e:
        print(f"error executing QUERY [Error : {e} ] ")

    db.commit()