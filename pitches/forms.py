from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pitches.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken')
        
    def validate_email(self, email):
        
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Login')
    
    
class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    bio = TextAreaField('Bio', validators=[DataRequired()])

    submit = SubmitField('Update')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        
        if user:
            raise ValidationError('Username is taken')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError('Email is taken')
        
class PitchForm(FlaskForm):      
    topic = SelectField('Topics',choices=[('Travel bucket list','Travel bucket list'),('Pickup lines','Pickup lines'),('Business pitch','Business pitch'), ('Technology pitch','Technology pitch'), ('Life changing ideas','Life changing ideas')])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
    
class CommentForm(FlaskForm):
    content = StringField('Add a comment', validators=[DataRequired()])
    upvote = BooleanField('Upvote')
    downvote = BooleanField('Downvote')
    submit = SubmitField('Comment')
    