from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def create_user():
    print('Got Post Info')
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    more_from_form = request.form['more']
    time_from_form = request.form['time']
    comment_from_form = request.form['comment']
    return render_template("result.html",
                           name_on_template=name_from_form,
                           location_on_template=location_from_form,
                           language_on_template=language_from_form,
                           more_on_template=more_from_form,
                           time_on_template=time_from_form,
                           comment_on_template=comment_from_form
                           )


if __name__ == "__main__":
    app.run(debug=True)
