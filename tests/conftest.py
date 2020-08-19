import pytest
pytest_plugins = ("tests.fix_api",)

from process_tests import TestProcess
from process_tests import wait_for_strings
@pytest.yield_fixture
def app_server(scope='session'):
    with TestProcess('python', 'app.py') as app_server:
        wait_for_strings(app_server.read, 10, "Running")
        yield app_server
