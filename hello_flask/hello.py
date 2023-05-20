from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/say/<name>')
def say(name):
    return "Hi, " + name


@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return ' '.join([word] * num)


@app.route('/<other>')
def other(other):
    return "Sorry! No response. Try again."


if __name__ == '__main__':

    app.run(debug=True)
