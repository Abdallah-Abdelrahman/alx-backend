#!/usr/bin/env python3
'''Module defines flask app'''
from flask import Flask
from flask_babel import Babel


class Config:
    '''class to set Bable's default locale and timezone'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
