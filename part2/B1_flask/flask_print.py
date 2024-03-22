from flask import Flask,request

app = Flask(__name__)#对象用于启动Flask

#函数是暴露在外面的接口
@app.route("/")#注释器，访问路径
def hello_world():
    return "hello word"

@app.route("/hllo")#注释器，访问路径http://127.0.0.1:5000/hllo
def hello_world2():
    return "hello word lichunyang"

@app.route("/hllo/<username>")#注释器，访问路径http://127.0.0.1:5000/hllo//传入的参数
def hello_world3(username):
    print(username)
    return "hello word lichunyang " + username

@app.route("/hllo/args/<username>")#注释器，访问路径http://127.0.0.1:5000/hllo/args/aaa?key=qqq
def hello_world4(username):
    print(username)#aaa
    key = request.args.get("key")
    print(key)#qqq
    return "hello word lichunyang " + username + ":::" + key

if __name__ == "__main__":
    app.run()
    # http://127.0.0.1:5000
    #127.0.0.1本地local
    #5000默认端口号