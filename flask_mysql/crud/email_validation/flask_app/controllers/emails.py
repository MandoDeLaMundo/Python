from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    emails = email.Email.get_all()
    return render_template('success.html', emails = emails)


@app.route('/register', methods=['post'])
def register():
    if not email.Email.validate_user(request.form):
        return redirect('/')
    email.Email.save(request.form)
    return redirect('/success')
