from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-my-very-secret-key'

env = 'pro'
if env == 'dev':
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/pitches'
 app.debug = True
else:
 app.debug = False
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://nistfehdirgxrx:ae412f0a7de50e43fd1096d7a0cf3967d9585beed5aa7c5d7cb96ce76614de2e@ec2-52-5-110-35.compute-1.amazonaws.com:5432/daglk5fjt7k082'

db = SQLAlchemy(app)
bc = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
from pitches import views