from flask import Flask
from app.register import registerApp


def create_app():
    app = Flask(__name__)
    registerApp(app)

    return app

apps = create_app()