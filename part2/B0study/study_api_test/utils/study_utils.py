#要从数据库拿到数据
#1.链接到数据库
import pymysql


def get_mysql_connection():
    db_info = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "mydb2",
        "charset": "utf8"
    }
    conn = pymysql.connect(**db_info)#这是链接方法和传入参数
    return conn

def get_mysql_case_data(interface_type):
    conn = get_mysql_connection()
    #拿到了连接以后，写sql语句读取数据
    sql = "select * from case_data where interface_type = '{}'".format(interface_type)
    cursor = conn.cursor()  # 游标
    cursor.execute(sql)#执行sql
    result = cursor.fetchall()  # 从数据库文件中提取元素
    return result