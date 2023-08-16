from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "QNT - Extractos 0.0.1 BETA"