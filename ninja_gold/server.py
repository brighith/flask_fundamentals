from flask import Flask, render_template, redirect, request, session
import random as rd
from datetime import datetime as dt

app = Flask(__name__)
app.secret_key = "ninja"


@app.route("/")
def start():
    if "gold" not in session:
        session['gold'] = 0
        session['list'] = []
        session['counter'] = 0
    gold = session['gold']
    list = session['list']
    return render_template('index.html', gold=gold, list=list)


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")


@app.route("/collect_money", methods=["POST"])
def collect_money():

    method = request.form['building']
    if method == "farm":
        amount = rd.randint(10, 20)
        now = dt.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        text = f"earned {amount} golds from the farm ! {timestamp}"

    elif method == "cave":
        amount = rd.randint(5, 10)
        now = dt.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        text = f"earned {amount} golds from the cave ! {timestamp}"

    elif method == "house":
        amount = rd.randint(2, 5)
        now = dt.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        text = f"earned {amount} golds from the house ! {timestamp}"

    elif method == "casino":
        amount = rd.randint(-50, 50)
        now = dt.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if amount > 0:
            text = f"earned {amount} golds from the casino ! {timestamp}"
        elif amount == 0:
            text = "you earned 0 gold"
        else:
            text = f"lost {amount} golds from the casino ! {timestamp}"
    session['list'].insert(0, text)
    session["gold"] += amount
    session['counter'] += 1
    return redirect("/")


@app.route('/reset', methods=['post'])
def reset():
    session['list'] = []
    session['building'] = None
    session['gold'] = 0
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
