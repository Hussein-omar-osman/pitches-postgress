from flask import Flask, render_template, url_for, flash, redirect
from pitches import app
from pitches import forms
from pitches.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/about")
def about():
 return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
 return render_template('register.html', title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 email = form.email.data
 password = form.password.data
 print(email, password)
 return render_template('login.html', title='Login', form=form)