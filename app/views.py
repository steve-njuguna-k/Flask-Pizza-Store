from app import app
from flask import render_template
from .forms import LoginForm, RegisterForm

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/register/')
def register():
    form = RegisterForm()
    return render_template('Register.html', form = form)

@app.route('/login/')
def login():
    form = LoginForm()
    return render_template('Login.html', form = form)

@app.route('/menu/')
def menu():
    return render_template('Menu.html')