import os
import tempfile

import pytest
from twitter_bot_app import create_app,db
from sqlalchemy import text
from twitter_bot_app.models import User, Word

@pytest.fixture
def app():
    """Setup code to create an app with some dummy data."""
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })
    
    with app.app_context():
        db.create_all()
        user1 = User(id_str='11', english=True, arabic=False, mon=True,sat=True)
        user2 = User(id_str='12', english=False, arabic=True,tues=True,fri=True)
        word1 = Word(word='semejanzas', language='Spanish', article="https://www.eldiario.es/sociedad/segunda-oleada-COVID-19-otono_0_1037646334.html")
        word2 = Word(word="蛋糕", language="mandarin_chinese_simplified", video="https://www.youtube.com/watch?v=nYQ5uc6plCs")

        db.session.add_all([user1,user2,word1,word2])
        yield app
        db.session.remove()
        db.drop_all()
    

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()