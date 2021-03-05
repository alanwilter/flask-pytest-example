from flask import jsonify

from pytest_cov.embed import cleanup_on_sigterm

cleanup_on_sigterm()


def configure_routes(app):
    @app.route("/")
    def hello_world():
        return jsonify(
            message="Hello World",
        )
