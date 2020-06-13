import sqlite3
import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.db_methods import *

user1 = User(id='11', subscribed=True, english=True, arabic=False)
user2 = User(id='12', subscribed=True, english=False, arabic=True)
def test_addNewUserWithLanguage(app):
    
    # the app that is yield from conftest is already in context!
        
    db.session.add(user1)
    db.session.commit()
    a = (User.query.first())
    assert a.id == user1.id
    db.session.delete(user1)
    db.session.commit()
    #print(User.query.all())

    #assert 'closed' in str(e.value)
def test_updateNewUser(app):
    updateUser(user1.id,english=True)
    user = User.query.first()
    assert user.id == user1.id
    assert user.english == True

def test_updateLanguageOfExistingUser(app):
    updateUser(user1.id,english=False)
    user = User.query.first()
    assert user.id == user1.id
    assert user.english == False

def test_removeUser(app):
    user = User.query.first()
    assert user.id == user1.id
    removeUser(user1.id)
    user = User.query.first()
    assert user == None


