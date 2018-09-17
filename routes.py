from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subpage')
def subpage():
    return render_template('subpage.html')