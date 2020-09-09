"""
Pytest plugin to interact with the api at http level
"""

import json
from urllib.parse import urljoin

import pytest
import requests

from process_tests import TestProcess
from process_tests import wait_for_strings
import time


@pytest.fixture(scope="session")
def app_server():
    with TestProcess("python", "app.py") as app_server:
        wait_for_strings(app_server.read, 10, "Running")
        # time.sleep(2)
        print(app_server.read())
        yield app_server
        print("\n>>>>Teardown app_service")
        app_server.close()


def pytest_addoption(parser):
    parser.addoption(
        "--api-url", help="api url to test [default: %(default)s]", default="http://localhost:5000",
    )


@pytest.fixture(scope="session")
def api_url(request):
    """
    Return the api url configured by --api-url
    """
    return request.config.getoption("--api-url").rstrip("/")


@pytest.fixture(scope="function")
def api(api_url, app_server):
    api = Api(api_url)
    yield api


class Api:
    def __init__(self, url=None):
        self.url = url
        self.session = requests.Session()
        self.logged_in = set()

    def get(self, url, data=None, headers=None):
        return self._request("get", url, data=data, headers=headers)

    def _request(
        self, method_name, url, data=None, headers=None,
    ):

        url = urljoin(self.url, url)

        hs = {"Content-Type": "application/json"}

        if headers is not None:
            hs.update(headers)

        method = getattr(self.session, method_name)
        if method_name in ("get", "options"):
            rv = method(url, params=data, headers=hs)
        elif method_name == "delete":
            if data:
                raise ValueError("data not supported with delete")
            rv = method(url, headers=hs)
        else:
            if data is not None:
                data = json.dumps(data)
            rv = method(url, data, headers=hs)
        return rv
