# Flask-APScheduler Test Server

This is a test server used to reproduce an issue with `flask-apscheduler` at version `1.12.3`. For further information, see the issue thread here: https://github.com/viniciuschiele/flask-apscheduler/issues/198


## Demo server with Docker

Use `./run.sh` on the terminal to build & run


## Demo server with virtual environment

1. Run `pip install -e .` in a virtual environment
1. Run `./entrypoint.sh` to start the gunicorn server
