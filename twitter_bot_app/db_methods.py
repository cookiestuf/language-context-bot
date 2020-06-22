from twitter_bot_app import db
from twitter_bot_app.models import User, Word
def updateUser(user_id, **kwargs):
    """
    Adds user with id to database. If id already in database, updates arguments passed into kwargs.
    Returns updated User python obj (tests rely on this functionality)
    """
    user_id = str(user_id)
    user = User.query.get(user_id)
    if user != None:
        User.query.filter_by(id=user_id).update(kwargs)
    else:
        user = User(id=user_id, **kwargs)
        db.session.add(user)    
    db.session.commit()
    return User.query.filter_by(id=user_id).first()
def deleteUser(user_id):
    """
    Removes user with id in database. does nothing if user DNE
    """
    user_obj = User.query.filter_by(id=user_id).first()
    if user_obj != None: # add some error catching here?
        db.session.delete(user_obj)
        db.session.commit()

def getUsersForLanguage(language):
    """
    Returns all subscribed users for language in a list.
    """

def getUser(user_id):
    """
    Return User object of given id
    """