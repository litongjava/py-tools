# *-* coding:utf-8 *-
import pymysql

# plisp
host = '192.168.3.9';
port = 3306
user = 'root'
passwd = 'robot_123456#'
db = 'ruoyi-vue-pro'
charset = 'utf8'

connection = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
cursor = connection.cursor()
try:
    execute = cursor.execute("show tables;")
    fetchall = cursor.fetchall()
    # print(fetchall)
    for i in fetchall:
        for table_name in i:
            sql = "show create table " + table_name
            cursor_execute = cursor.execute(sql)
            cursor_fetchall = cursor.fetchall()
            print(type(cursor_fetchall));
            # print(cursor_fetchall)
            for k in cursor_fetchall:
                for l in k:
                    print(type(l), type(k))


finally:
    cursor.close()
    connection.close()
