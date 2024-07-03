#!/usr/bin/env python3
'''Module defines flask app'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
