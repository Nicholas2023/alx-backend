#!/usr/bin/env python3
"""
A module that implements class config
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """
    A class that implements different languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match of site languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """
    Renders the html doc
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
