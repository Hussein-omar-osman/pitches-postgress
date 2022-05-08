from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628b453b0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

from pitches import views