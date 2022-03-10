from flask import Blueprint

hello = Blueprint('hello', __name__)


@hello.get('/')
def heloWorld():
    return 'Hello Wolrd'
