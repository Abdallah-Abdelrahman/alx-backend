#!/usr/bin/env python3
'''Module defines flask app'''
from typing import Any, Dict, Union
from flask import Flask, request, render_template, g
from flask_babel import Babel

users: Dict[int, Dict[str, Any]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    user = get_user()

    if lang in app.config.get('LANGUAGES'):
        # locale from URL
        return lang
    if user and user.get('locale') in app.config.get('LANGUAGES'):
        # locale from user settings
        return user.get('locale')

    # locale from header
    return request.accept_languages.best_match(app.config.get('LANGUAGES'))


@app.route('/')
def index():
    '''render index template'''
    return render_template('6-index.html', user=g.user)


def get_user() -> Union[Dict[str, str], None]:
    '''returns a user dictionary or None'''
    id_ = request.args.get('login_as')

    if not id_ or not id_.isnumeric():
        return None
    return users.get(int(id_))


@app.before_request
def before_request() -> None:
    '''find a user if any, and set it as a global on `flask.g.user`'''
    setattr(g, 'user', get_user())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
