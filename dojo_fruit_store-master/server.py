from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['post'])
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    blackberry = request.form['blackberry']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    now = datetime.datetime.now()
    timer = now.strftime("%Y-%m-%d %H:%M")
    return render_template("checkout.html", strawberry=int(strawberry), raspberry=int(raspberry), apple=int(apple), blackberry=int(blackberry), first_name=firstName, last_name=lastName, student_id=studentId, times=timer)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
