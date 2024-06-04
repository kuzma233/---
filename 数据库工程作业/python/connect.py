import pymysql
def connect():
    conn = pymysql.connect(host='localhost', user='root',password='123456',database='library')#连接数据库library
    cursor = conn.cursor()
    return cursor, conn