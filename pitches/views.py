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
 form = RegistrationForm()
 
 # print(username, email, password)
 if form.validate_on_submit():
  flash(f'Account created for {form.username.data}', 'primary')
  return redirect(url_for('home'))
 return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 email = form.email.data
 password = form.password.data
 # print(email, password)
 if form.validate_on_submit():
  if form.email.data == 'husseinomar6190@gmail.com' and form.password.data == '123':
   flash(f'Successfuly Logged in', 'primary')
   return redirect(url_for('home'))
  else:
   flash(f'Login unsuccessfuly', 'danger')
 return render_template('login.html', title='Login', form=form)