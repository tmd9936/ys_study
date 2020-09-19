
# test_request_context() : Flask에 있는 메소드
# HTTP요청을 테스트 할 수 있는 메소드
# url_for() 

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/hello")
def test():
    return "<h1>Hello World!</h1>"

@app.route("/user/<username>")
def get_user(username):
    return "user:"+ username

if __name__ == "__main__":
    with app.test_request_context():
        # 위에있는 test함수(루트)
        print(url_for("test"))
        # 위에있는 get_user함수(루트), 인자값 username을 지정
        print(url_for("get_user", username = "kim"))