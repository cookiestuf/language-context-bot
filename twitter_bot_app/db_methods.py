from twitter_bot_app import db
from twitter_bot_app.models import User, Word
def updateUser(id, **kwargs):
    """
    Adds user with id to database. If id already in database, updates arguments passed into kwargs
    """

def removeUser(id):
    """
    Removes user with id in database. If id not in database --> ignore
    """

def getUsersForLanguage(language):
    """
    Returns all subscribed users for language in a list.
    """

def getUser(id):
    """
    Return User object of given id
    """