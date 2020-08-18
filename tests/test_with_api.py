from flask import Flask
import json

from handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'{"message":"Hello World"}\n'
    assert response.status_code == 200

def test_api(api):
    resp = api.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message":"Hello World"}
