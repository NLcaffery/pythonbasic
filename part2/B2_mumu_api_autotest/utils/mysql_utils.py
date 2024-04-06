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
#需要获取的测试用例，属性是interface_type的行
def get_mysql_case_data (interface_type):
    conn = get_sql_connection()
    sql = "select * from case_data where interface_type = '{}'".format(interface_type)#传进来的字符串需要用单引号包裹起来
    cursor = conn.cursor()#游标
    cursor.execute(sql)
    result = cursor.fetchall()#从数据库文件中提取元素
    return result