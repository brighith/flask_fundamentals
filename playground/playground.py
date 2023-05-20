from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"


@app.route("/play")
def play_ground():
    return render_template("index.html", times=3, b_gc="blue")


@app.route("/play/<int:x>")
def play_ground_x(x):
    return render_template("index.html", times=x, b_gc="blue")


@app.route("/play/<int:x>/<color>")
def play_color(x, color):
    return render_template("index.html", times=x, b_gc=color)


if __name__ == "__main__":
    app.run(debug=True)
