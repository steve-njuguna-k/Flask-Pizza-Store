from app import app
from flask import render_template
from .forms import RegisterForm

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/register/')
def register():
    form = RegisterForm()
    return render_template('Register.html', form = form)

@app.route('/login/')
def login():
    return render_template('Login.html')