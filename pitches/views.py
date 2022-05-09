import email
from flask import Flask, render_template, url_for, flash, redirect
from pitches import app, db, bc
# from pitches import forms
from pitches.forms import LoginForm, RegistrationForm
from pitches.models import User, Post, Comments

@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/about")
def about():
 return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
 form = RegistrationForm()
 
 
 if form.validate_on_submit():
  hashed_pass = bc.generate_password_hash(form.password.data).decode('utf-8')
  user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
  db.session.add(user)
  db.session.commit()
  flash(f'Account has neen created for {form.username.data}. Now you can login', 'primary')
  return redirect(url_for('login'))
 return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 
 if form.validate_on_submit():
  if form.email.data == 'husseinomar6190@gmail.com' and form.password.data == '123':
   flash(f'Successfuly Logged in', 'primary')
   return redirect(url_for('home'))
  else:
   flash(f'Login unsuccessfuly', 'danger')
 return render_template('login.html', title='Login', form=form)