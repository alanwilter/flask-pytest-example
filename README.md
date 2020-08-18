# Flask Pytest routing and requests example
Simple sample application demonstrating how to use Pytest with Flask for testing routing and requests.
The example includes a basic "hello world" route to demonstrate a GET request. Using local Pytest api plugin.

## Setup and run instructions
Use virtualenv or your environment of choice

```bash
git clone https://github.com/alanwilter/flask-pytest-example

cd flask-pytest-example

pip install -r requirements.txt

# Start app in another terminal
python app.py

# Then run:
pytest --cov --cov-report term-missing -k via | grep routes

# handlers/routes.py           6      0   100%

# then compare with

pytest --cov --cov-report term-missing -k via | grep routes

# handlers/routes.py           6      2    67%   8-10
```
