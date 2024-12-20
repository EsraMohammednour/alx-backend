#!/usr/bin/env python3
'''Module thatconfigure available languages in our app'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''class that using for set lang'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''display page'''
    return render_template('1-index.html')
