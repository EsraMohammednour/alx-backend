#!/usr/bin/env python3
'''Module that create sigle route'''
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    '''display templete haning Hello world'''
    return render_template('0-index.html')
