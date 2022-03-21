from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def root():


    return render_template ('ooof.html')

@app.route('/I_gotcha_baby')
def result():
    return render_template ('sumbit.html')






@app.route('/something', methods = ["post"])

def submit():
    session['ajgfha'] = request.form['ayee']

    session['asumadre'] = request.form['ahj']

    session['session_language'] = request.form['name_language']

    
    session['opsk'] = request.form['jdryjde']
    return redirect ('/I_gotcha_baby')




if __name__ == "__main__":
    app.run (debug = True)