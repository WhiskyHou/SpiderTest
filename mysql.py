# encoding=utf-8

import MySQLdb

hostname = "localhost"
user = "root"
password = ""
dbname = "spidert_test"
tablename = "data"
port = 3306
char = "utf8"

connection = MySQLdb.connect(host=hostname, user=user, passwd=password, db=dbname, port=port, charset=char)
cursor = connection.cursor()
# cursor.execute('SELECT * FROM data')
# data = cursor.fetchone()
# print data
try:
    cursor.execute('INSERT INTO data(url, title, content) VALUES("http://baidu.com", "baidu", "a famous it company")')
    connection.commit()
    print("insert success")
except:
    print("insert error")
cursor.execute('SELECT * FROM data')
data2 = cursor.fetchall()
print(data2)
