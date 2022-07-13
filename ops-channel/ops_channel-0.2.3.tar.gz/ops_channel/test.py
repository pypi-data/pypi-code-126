
from base import *


# a=cli.render('''
#    my name is {{name}}.
#    {%- for i in [1,2,3,4,5,6,7] %}
#     {{i}}
#    {%- endfor %}
# ''',{'name':"jqzhang"})
#
# # print(a)
#
#
# dsn='mysql://root:root@localhost:3306/ferry'
#
# conn=cli.get_mysql_connection(dsn)
# print(cli.mysql_query(conn,'show tables'))
# print(cli.mysql_query(conn,'select * from test'))



# conn=cli.get_sqlite_connection(":memory:")
#
# cli.sqlite_query(conn,'''
# CREATE TABLE COMPANY(
#    ID INT PRIMARY KEY     NOT NULL,
#    NAME           TEXT    NOT NULL,
#    AGE            INT     NOT NULL,
#    ADDRESS        CHAR(50),
#    SALARY         REAL
# );
# ''')

# i="insert into COMPANY(NAME,ID,AGE) values('jqzhang','1',30)"
# cli.sqlite_query(conn,i)
# i="insert into COMPANY(NAME,ID,AGE) values('hello','2',35)"
# cli.sqlite_query(conn,i)

# sql='''
# INSERT INTO COMPANY (`ID`,`NAME`,`AGE`,`ADDRESS`,`SALARY`)
# VALUES
# (1,'jqzhang',30,NULL,NULL),
# (2,'hello',35,NULL,NULL);'''
# cli.sqlite_query(conn,sql)
#
# rows=cli.sqlite_query(conn,'select * from COMPANY')
#
# print(cli.dict2sql('COMPANY',rows))
#
#
# dsn = os.environ.get("DSN", "mysql://root:root@127.0.0.1:3306/pjm_db")
#
# dsn='mysql://root:root@localhost:3306/ferry'
# conn=cli.get_mysql_connection(dsn)
# cli.dump_mysql_data(conn,"/tmp/ferry")
# cli.dump_mysql_ddl(conn,"/tmp/ferry")



