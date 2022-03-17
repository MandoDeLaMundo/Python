from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/result')
def result():
    return render_template ('result.html')



@app.route('/submit', methods = ["post"])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/result')




if __name__ == "__main__":
    app.run (debug = True)