import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import logging
db = SQLAlchemy()
migrate = Migrate(compare_type = True)
load_dotenv()

def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(app.instance_path, 'twitter_bot_app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # TODO: Add test_config stuff for testing? See flask tutorial


    db.init_app(app)
    migrate.init_app(app, db)
    if __name__ == "__main__":
        print("create_app ran directly")
    else:
        print("create_app ran from import %s" % __name__)
    from . import models
    from . import twitter_conn

    # set up logging so that local and deployed testing outputs are equal
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    print("log level: %s" % gunicorn_logger.level)

    app.register_blueprint(twitter_conn.bp)
    return app