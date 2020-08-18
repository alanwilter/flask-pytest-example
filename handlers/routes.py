from flask import request
from flask import jsonify
import json


def configure_routes(app):

    @app.route('/')
    def hello_world():
        return jsonify(message='Hello World',)
