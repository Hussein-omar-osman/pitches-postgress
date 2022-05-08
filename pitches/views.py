from flask import Flask, render_template, url_for, flash, redirect
from pitches import app

@app.route('/')
def home():
 return render_template('home.html', title='Home')