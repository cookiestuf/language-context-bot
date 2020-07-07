from twitter_bot_app import db
from twitter_bot_app.models import User, Word
def updateUser(id_str, **kwargs):
    """
    Adds user with id_str to database. If id_str already in database, updates arguments passed into kwargs.
    Returns updated User python obj (tests rely on this functionality)
    """
    id_str=str(id_str)
    user = User.query.filter_by(id_str=id_str).first()
    if user != None:
        User.query.filter_by(id_str=id_str).update(kwargs)
    else:
        user = User(id_str=id_str, **kwargs)
        db.session.add(user)    
    db.session.commit()
    return User.query.filter_by(id_str=id_str).first()
def deleteUser(id_str):
    """
    Removes user with id_str in database. does nothing if user DNE
    """
    user_obj = User.query.filter_by(id_str=id_str).first()
    if user_obj != None: # add some error catching here?
        db.session.delete(user_obj)
        db.session.commit()

def getUsersForLanguage(language):
    """
    Returns all subscribed users for language in a list.
    """

def getUser(id_str):
    """
    Return User object of given id_str
    """