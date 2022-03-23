from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models import survey

@app.route('/')
def root():
    return render_template ('index.html')

@app.route('/result')
def result():
    return render_template ('result.html')



@app.route('/submit', methods = ["post"])
def submit():
    if not survey.Survey.validate_survey(request.form):
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    survey.Survey.save(request.form)
    return redirect ('/result')


