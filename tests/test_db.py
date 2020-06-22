import sqlite3
import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.db_methods import *

def test_updateNewUser(app):    
    # FYI the app that is yield from conftest is already in context!
    user = User(id='5000',french=True)
    db_user = updateUser(user_id='5000', french=True)
    assert db_user.id == user.id
    assert db_user.french == user.french
    assert db_user.subscribed == user.subscribed
    db.session.delete(db_user)
    db.session.commit()

def test_updateLanguageOfExistingUser(app):
    existing_user = User.query.first()
    assert existing_user.spanish != True
    existing_user = updateUser(existing_user.id,spanish=True)
    assert existing_user.spanish == True
    updateUser(existing_user.id,spanish=False) # change to original setup 

def test_deleteUser(app):
    existing_user = User.query.first()
    existing_user = User.query.filter_by(id=existing_user.id).first()
    assert existing_user != None
    deleteUser(existing_user.id)
    deleted_user = User.query.get(existing_user.id)
    assert deleted_user == None
    # add back user. change to original setup
    db.session.add(existing_user)
    db.session.commit()

def test_deleteUserThatDNE(app):
    dne_user = User(id='5000',french=True)
    no_user = User.query.get(dne_user.id)
    assert no_user == None
    assert deleteUser(dne_user.id) == True #no error thrown!
