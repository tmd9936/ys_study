from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/user/<username>")
def user(username):
    return render_template('user.html', username1=username)

if __name__ == '__main__':
    app.run(debug=True)