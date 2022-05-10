from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628b453b0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/pitches'

db = SQLAlchemy(app)
bc = Bcrypt(app)
migrate = Migrate(app, db)
lm = LoginManager(app)
lm.login_view = 'login'
lm.login_message_category = 'danger'
from pitches import views