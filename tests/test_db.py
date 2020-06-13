import sqlite3
import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.db_methods import *

def test_updateNewUser(app):    
    # the app that is yield from conftest is already in context!
    test_user = User(id='5000', subscribed=True, english=True, arabic=False, mon=True,sat=True)
    updateUser(test_user.id, french=True)
    db_user = User.query.get(test_user.id)
    assert db_user.id == test_user.id
    assert db_user.french == test_user.french
    assert db_user.subscribed == test_user.subscribed
    db.session.delete(user1)
    db.session.commit()

def test_updateLanguageOfExistingUser(app):
    existing_user = User.query.first()
    assert existing_user.spanish == False
    updateUser(existing_user.id,spanish=True)
    user = User.query.get(existing_user.id)
    assert existing_user.spanish == True
    updateUser(existing_user.id,spanish=False) # change to original setup 

def test_removeUser(app):
    existing_user = User.query.first()
    assert existing_user != None
    removeUser(existing_user.id)
    removed_user = User.query.get(existing_user.id)
    assert removed_user == None
    # add back user. change to original setup
    db.session.add(existing_user)
    db.session.commit()

