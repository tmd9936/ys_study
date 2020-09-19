from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/helpdesk")
def helpdesk():
    return render_template('helpdesk.html', title='Helpdesk')



if __name__ == "__main__":
    app.run(debug=True)