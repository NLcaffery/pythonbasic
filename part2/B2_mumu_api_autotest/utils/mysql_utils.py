#一些操控数据库的方法
import pymysql
def get_sql_connection():
    db_info = {
        "host":"localhost",
        "user":"root",
        "password":"root",
        "database":"mydb2",
        "charset":"utf8"
    }
    conn = pymysql.connect(**db_info)
    return conn

def get_mysql_case_data (interface_type):
    conn = get_sql_connection()
    sql = "select * from case_data where interface_type = '{}'".format(interface_type)
    cursor = conn.cursor()#游标
    cursor.execute(sql)
    result = cursor.fetchall()#从数据库文件中提取元素
    return result