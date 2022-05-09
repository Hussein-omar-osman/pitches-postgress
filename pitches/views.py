import email
from flask import Flask, render_template, url_for, flash, redirect, request
from pitches import app, db, bc
# from pitches import forms
from pitches.forms import LoginForm, RegistrationForm
from pitches.models import User, Post, Comments
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
 return render_template('home.html', title='Home')

@app.route("/about")
def about():
 return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))    
  form = RegistrationForm()

  if form.validate_on_submit():
    hashed_pass = bc.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
    db.session.add(user)
    db.session.commit()
    flash(f'Account has neen created for {form.username.data}', 'primary')
    login_user(user)
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 if current_user.is_authenticated:
   return redirect(url_for('home'))
 form = LoginForm()
 
 if form.validate_on_submit():
  user = User.query.filter_by(email=form.email.data).first()
  if user and bc.check_password_hash(user.password, form.password.data):
      login_user(user)
      flash(f'{user.username}, You have been logged in!', 'primary')
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
  else:
      flash('Login Unsuccessful. Please check email and password', 'danger')
 return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('home'))
  
  
@app.route("/account")
@login_required
def account():
  return render_template('account.html', title='Account')