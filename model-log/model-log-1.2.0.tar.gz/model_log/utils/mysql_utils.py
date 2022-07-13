
import pymysql
import socket
import time


class MySQLDao:

    def __init__(self, db_host, db_port, db_username, db_password, data_base):
        self.db_host = db_host
        self.db_port = db_port
        self.db_username = db_username
        self.db_password = db_password
        self.data_base = data_base

    def create_conn_with_dict(self):
        conn = pymysql.connect(host=self.db_host, port=self.db_port, user=self.db_username, password=self.db_password, database=self.data_base, charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        return conn

    def query(self, sql):
        conn = self.create_conn_with_dict()

        results = []
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    def execute(self, sql):
        conn = self.create_conn_with_dict()

        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()

    def batchAddRows(self, tb_name, rows):
        conn = self.create_conn_with_dict()
        if len(rows) > 0:
            
            cursor = conn.cursor()
            keys = rows[0].keys()
            v_keys = ','.join(['%%(%s)s' % key for key in keys])
            sql = "INSERT INTO %s (%s) VALUES(%s)" % (tb_name, ','.join(keys), v_keys)
            # print sql
            cursor.executemany(sql, rows)

            conn.commit()
            cursor.close()
            conn.close()
            return True
        return False



if __name__ == "__main__":
    pass
