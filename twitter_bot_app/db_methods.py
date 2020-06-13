from twitter_bot_app import db
from twitter_bot_app.models import User, Word
def updateUser(user_id, **kwargs):
    """
    Adds user with id to database. If id already in database, updates arguments passed into kwargs
    """
    user = User.query.get(user_id)
    if user != None:
        user.update(kwargs)
    #db.session.add(id=user_id, **kwargs)    

def removeUser(user_id):
    """
    Removes user with id in database. If id not in database --> ignore
    """

def getUsersForLanguage(language):
    """
    Returns all subscribed users for language in a list.
    """

def getUser(user_id):
    """
    Return User object of given id
    """