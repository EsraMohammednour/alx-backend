#!/usr/bin/env python3
'''Module thatconfigure available languages in our app'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''class that using for set lang'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_pyfile('babel.cfg')
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Funtion that get locate'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''display page'''
    return render_template('3-index.html')
