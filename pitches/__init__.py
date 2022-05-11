from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-my-very-secret-key'

env = 'dev'
if env == 'dev':
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/pitches'
 app.debug = True
else:
 app.debug = False

db = SQLAlchemy(app)
bc = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
from pitches import views