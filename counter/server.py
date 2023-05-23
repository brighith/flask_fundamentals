from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("show.html", count=session['count'])


@app.route('/add')
def add():
    session['count'] += 1
    return redirect('/')


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
