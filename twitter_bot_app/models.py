# from sqlalchemy import db.Column, Integer, String, db.Boolean
from twitter_bot_app import db
#from db import db.Column, Integer, String, db.Boolean

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Text(), primary_key=True, autoincrement=False)
    subscribed = db.Column(db.Boolean)
    english = db.Column(db.Boolean)
    arabic = db.Column(db.Boolean)
    french = db.Column(db.Boolean)
    german = db.Column(db.Boolean)
    hindi = db.Column(db.Boolean)
    mandarin_chinese = db.Column(db.Boolean)
    portuguese = db.Column(db.Boolean)
    spanish = db.Column(db.Boolean)
    arabic = db.Column(db.Boolean)
    dutch = db.Column(db.Boolean)
    russian = db.Column(db.Boolean)
    italian = db.Column(db.Boolean)
    japanese = db.Column(db.Boolean)
    mon = db.Column(db.Boolean)
    tues = db.Column(db.Boolean)
    wed = db.Column(db.Boolean)
    thurs = db.Column(db.Boolean)
    fri = db.Column(db.Boolean)
    sat = db.Column(db.Boolean)
    sun = db.Column(db.Boolean)

    def __repr__(self):
        return "<User(id='%s')" % (self.id)

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Text(), primary_key=True)
    word = db.Column(db.Text(),nullable=False)
    langauge = db.Column(db.Text(), nullable=False)
    article = db.Column(db.Text())
    video = db.Column(db.Text())
    song = db.Column(db.Text())
