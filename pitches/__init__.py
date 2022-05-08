from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628b453b0b13ce0c676dfde280ba245'
from pitches import views