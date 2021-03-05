# Flask Pytest routing and requests example
Simple sample application demonstrating how to use Pytest with Flask for testing routing and requests.
The example includes a basic "hello world" route to demonstrate a GET request. Using local Pytest api plugin.

## Setup and run instructions
``` bash
# Not needed if using GitPod
python3 -m venv venv
source venv/bin/activate
git clone https://github.com/alanwilter/flask-pytest-example
cd flask-pytest-example
# end GitPod

pip install --upgrade pip
pip install -r requirements.txt

# Start app to check if it's OK
python app.py
# crtl-c

# Then run:
pytest --cov handlers --cov-report term-missing -k via -sv

# handlers/routes.py           6      0   100%
```
This now works with `pytest-cov` where `pytest` and `app` service run in separated processes.
