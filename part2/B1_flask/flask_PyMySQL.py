import pymysql
from flask import Flask

#mysql的基本连接信息
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydb1',
    charset='utf8'
)

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")
def holl_word():
    sql = "select + from scholl"
    result = cursor.execute(sql)
    r = cursor.fetchall()
    return str(r)

if __name__ == "__main__":
    app.run()