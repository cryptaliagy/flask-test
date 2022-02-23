import secrets
import logging

from flask import (
    Flask,
    jsonify,
)
from flask_apscheduler import (
    APScheduler
)

class Config:
    SECRET_KEY = secrets.token_hex(16)
    ENV = 'development'
    SCHEDULER_API_ENABLED = True


cron = APScheduler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    cron.init_app(app)

    @app.route('/heartbeat')
    def heartbeat():
        return jsonify(
            ok=True,
            msg='Service is up!'
        )

    @cron.task('interval', id='test', seconds=10)
    def task():
        logger.debug('Firing off task!')

    cron.start()

    return app
