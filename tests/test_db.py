import sqlite3
import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.db_methods import *

def test_updateNewUser(app):    
    # FYI the app that is yield from conftest is already in context!
    user = User(id_str='5000',french=True)
    db_user = updateUser(id_str='5000', french=True)
    assert db_user.id_str == user.id_str
    assert db_user.french == user.french
    db.session.delete(db_user)
    db.session.commit()

def test_updateLanguageOfExistingUser(app):
    existing_user = User.query.first()
    assert existing_user.spanish != True
    existing_user = updateUser(existing_user.id_str,spanish=True)
    assert existing_user.spanish == True
    updateUser(existing_user.id_str,spanish=False) # change to original setup 

def test_deleteUser(app):
    test_user = updateUser(id_str='5000', french=True)
    assert test_user.id_str == '5000'
    deleteUser(test_user.id_str)
    deleted_user = User.query.get(test_user.id_str)
    assert deleted_user == None

def test_deleteUserThatDNE(app):
    dne_user = User(id_str='5000',french=True)
    no_user = User.query.get(dne_user.id_str)
    assert no_user == None
    deleteUser(dne_user.id_str)
