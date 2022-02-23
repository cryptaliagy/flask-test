import secrets
import logging

from flask import (
    Flask,
    jsonify,
    request,
)
from flask_apscheduler import (
    APScheduler
)

class Config:
    SECRET_KEY = secrets.token_hex(16)
    ENV = 'development'
    SCHEDULER_API_ENABLED = True
    SCHEDULER_ALWAYS_START = True


cron = APScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    cron.init_app(app)

    app.logger.setLevel(logging.DEBUG)

    @app.route('/heartbeat')
    def heartbeat():
        return jsonify(
            ok=True,
            msg='Service is up!'
        )

    @cron.task('interval', id='some_test', seconds=10, misfire_grace_time=300)
    def task():
        app.logger.debug('Firing off task!')

    @app.before_request
    def _():
        app.logger.debug('Hit route %s', request.url)
        if not cron.running:
            cron.start()

    cron.start()

    return app
