from flask import Flask, request

app = Flask(__name__)

@app.route("/mypost", methods = ["post"])#指定方法
def my_post():
    #表单数据类型
    username = request.form["username"]
    # 平时用的更多的是json类型的数据模式
    request_data = request.get_json()
    return "post request" + username



if __name__ == "__main__":
    app.run(port=5555)#指定端口号