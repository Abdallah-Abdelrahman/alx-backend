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
    if lang in app.config.get('LANGUAGES'):
        return lang
    return request.accept_languages.best_match(app.config.get('LANGUAGES'))


@app.route('/')
def index():
    '''render index template'''
    return render_template('5-index.html', user=g.user)


def get_user(id_: int) -> Union[Dict[str, str], None]:
    '''returns a user dictionary or None'''
    return users.get(id_)


@app.before_request
def before_request() -> None:
    '''find a user if any, and set it as a global on `flask.g.user`'''
    id_ = request.args.get('login_as')

    if id_ and id_.isnumeric():
        id_ = int(id_)
    # set user on flask global
    setattr(g, 'user', get_user(id_))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
