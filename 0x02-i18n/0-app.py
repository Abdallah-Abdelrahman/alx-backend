#!/usr/bin/env python3
'''Module defines flask app'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    '''render index page'''
    return render_template('0-index.html')
