from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', x=8, y=8, c1="red", c2="black")


@app.route('/4')
def four():
    return render_template('index.html', x=4, y=8, c1="red", c2="black")


@app.route('/<int:x>/<int:y>')
def dynamic(x, y):
    return render_template('index.html', x=x, y=y)


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def color(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, c1=color1, c2=color2)


if __name__ == "__main__":
    app.run(debug=True)
