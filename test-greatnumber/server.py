from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = 'stay away from'


@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1, 100)
    if 'name' not in session:
        session['name'] = 0
    if 'attempts' not in session:
        session['attempts'] = 0
    print(session['random'])
    return render_template('index.html', random=session['random'], number=session['name'], attempts=session['attempts'])


@app.route('/process', methods=['post'])
def process():
    session['name'] = int(request.form['name'])
    session['attempts'] += 1
    return redirect('/')


@app.route('/lose', methods=['post'])
def lose():
    session.clear()
    return redirect('/')


@app.route('/clear', methods=['post'])
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
