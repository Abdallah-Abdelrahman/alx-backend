#!/usr/bin/env python3
'''Module defines flask app'''
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    '''Configuration class for Babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    lang = request.args.get('locale')
    if lang in app.config.get('LANGUAGES'):
        return lang
    return request.accept_languages.best_match(app.config.get('LANGUAGES'))


@app.route('/')
def index():
    '''render index template'''
    return render_template('4-index.html')
