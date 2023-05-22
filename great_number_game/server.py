from flask import Flask, session, request, redirect, render_template
import random


app = Flask(__name__)
app.secret_key = 'stay away from'


@app.route('/')
def start():
    if 'random' not in session:
        session['random'] = random.randrange(0, 101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    if session['random'] > int(request.form['guess']):
        result = "Too low"
        return render_template("index.html", result=result)

    elif session['random'] == int(request.form['guess']):
        result = "You Win"
        return render_template("index.html", result=result)

    else:
        result = "Too high"
        return render_template("index.html", result=result)


app.run(debug=True)
