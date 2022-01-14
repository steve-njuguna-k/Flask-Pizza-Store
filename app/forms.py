from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=255,  message='⚠️ Username length must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Username"})
    email = StringField(label='Email Address', validators=[DataRequired(), Email(message='⚠️ Enter A Valid Email Address!')], render_kw={"placeholder": "Email Address"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=255,  message='⚠️ Password strength must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password', message='⚠️ The Passwords Entered Do Not Match!')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField(label=('Sign Up'))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')       