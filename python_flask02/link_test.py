from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', title='Home')
# @app.route("/")
# @app.route("/")
# @app.route("/")



if __name__ == "__main__":
    app.run(debug=True)