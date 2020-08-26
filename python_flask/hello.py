'''
파이썬의 웹프레임워크

Flask : 웹프로그래밍에 있어서 가장 핵심적인 요소만을 포함하고 있는 프레임 워크
    (Micro Framework)

Django : 웹프로스래밍을 할 떄 필요로 하는 모든것들을 종합적으로
         갖추고 있는 프레임워크 (Full Stack Framework)


'''

from flask import Flask

app = Flask(__name__)

# 라우팅 : 복잡한 URI를 쉽게 처리하도록 하는 기능
@app.route("/")
@app.route("/hello/")
def hello():
    return "<em>Hello World123!!</em>"



if __name__ == "__main__":
    app.run(debug=True)



