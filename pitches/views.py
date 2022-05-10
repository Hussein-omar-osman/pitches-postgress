import smtplib
from importlib.resources import contents
from flask import Flask, render_template, url_for, flash, redirect, request
from pitches import app, db, bc
# from pitches import forms
from pitches.forms import LoginForm, RegistrationForm, UpdateProfileForm, PitchForm, CommentForm
from pitches.models import User, Post, Comments
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
 posts = Post.query.order_by(Post.date_posted.desc()).all() 
 return render_template('home.html', title='Home', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    users = User.query.all()
    if form.validate_on_submit():
        hashed_password = bc.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        my_email = 'bazub702@gmail.com'
        my_password = 'mwas6190'
        content = 'I am very exicted to see you create an account thtanks'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=user.email,
                            msg=f'Subject:{user.username}: Welcome to flask blog\n\n {content}')
        flash(f'Account created for {form.username.data}! You can Log in', 'success')
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form, users=users)

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
  
  
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
  return render_template('account.html', title='Account')

@app.route("/update_profile", methods=['GET', 'POST'])
@login_required
def update_profile():
  form = UpdateProfileForm()
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.email = form.email.data
    current_user.description = form.bio.data
    db.session.commit()
    flash('Your account has been updated', 'primary')
    return redirect(url_for('account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.bio.data = current_user.description
    
  return render_template('update_profile.html', title='Update Profile', form=form)

@app.route("/create_pitch", methods=['GET', 'POST'])
@login_required
def create_pitch():
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Post(topic=form.topic.data, content=form.content.data, author=current_user)
    db.session.add(pitch)
    db.session.commit()
    flash('You have posted', 'primary')
    return redirect(url_for('home'))
    
  return render_template('create_pitch.html', title='Create Pitch', form=form)

@app.route("/post/<post_id>" , methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comments.query.order_by(Comments.date_posted.desc()).filter_by(post_id=post_id)
    form = CommentForm()
    if form.validate_on_submit():
      if form.upvote.data:
        recent = post.likes
        new = recent + 1
        post.likes = new
        db.session.commit()
        
      if form.downvote.data:
        recent = post.dislikes
        new = recent + 1
        post.dislikes = new
        db.session.commit()
        
      comment = Comments(content=form.content.data, user_comments=current_user, post_id=post_id)
      db.session.add(comment)
      db.session.commit()
      flash('You have commented', 'primary')
      return redirect(url_for('post', post_id=post_id))
    return render_template('post.html', post=post, form=form, comments=comments)

