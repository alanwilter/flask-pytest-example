from flask import request
from flask import jsonify
import json

from pytest_cov.embed import cleanup_on_sigterm

cleanup_on_sigterm()


def configure_routes(app):
    @app.route("/")
    def hello_world():
        return jsonify(message="Hello World",)
