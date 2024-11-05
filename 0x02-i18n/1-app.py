#!/usr/bin/env python3
'''Module thatconfigure available languages in our app'''
 from flask import Flask, render_template
 from flask_babel import Babel


app = Flask(__name__)
class Config:
    '''class that using for set lang'''
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)
@app.route('/')
def index():
    '''display page'''
    return render_template('1-index.html')
