from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628b453b0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/pitches'

db = SQLAlchemy(app)
bc = Bcrypt(app)
lm = LoginManager(app)
from pitches import views