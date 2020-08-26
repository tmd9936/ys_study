from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>hello world!!</h1>'

# user_name 파라미터의 타입은 String(기본값)
@app.route("/user/<user_name>")
def get_uriName(user_name):
   return 'user : ' + user_name

# post_id 파라미터는 int형 타입
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'Post %d' % post_id

# pi 파라미터는 float형 타입
@app.route("/circle/<float:pi>")
def show_pi(pi):
    return 'PI %f' % pi

if __name__ == "__main__":
    app.run(debug=True, port=9000)