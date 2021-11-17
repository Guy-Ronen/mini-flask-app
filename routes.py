from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Email
from models import User
from app import app, db

class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators = [DataRequired()])
    password = PasswordField(label = 'Password', validators = [DataRequired()])
    submit = SubmitField(label = 'Login')

class RegisterForm(FlaskForm):
    first_name = StringField(label = 'First Name', validators = [DataRequired()])
    last_name = StringField(label = 'Last Name', validators = [DataRequired()])
    email = StringField(label = 'Email', validators = [DataRequired()])
    password = PasswordField(label = 'Password', validators = [DataRequired()])
    password2 = PasswordField(label = 'Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField(label = 'Register')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and (user.password == form.password.data):
            return redirect(f'/sucsess/{user.id}')
    return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, password = form.password.data, first_name = form.first_name.data, last_name = form.last_name.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/sucsess/<int:user_id>', methods = ['GET', 'POST'])
def sucsess(user_id):
    user = User.query.filter_by(id = user_id).first()
    print(user.first_name)
    return render_template('sucsess.html', user = user)