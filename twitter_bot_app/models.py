# from sqlalchemy import db.Column, Integer, String, db.Boolean
from twitter_bot_app import db
#from db import db.Column, Integer, String, db.Boolean

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True, autoincrement=False)
    subscribed = db.Column(db.Boolean)
    english = db.Column(db.Boolean)
    arabic = db.Column(db.Boolean)
    french = db.Column(db.Boolean)
    german = db.Column(db.Boolean)
    hindi = db.Column(db.Boolean)
    mandarin_chinese_simplified = db.Column(db.Boolean)
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
        class_variables = vars(self)
        user_str = "<User(id='%s'" % (self.id)

        for var,val in class_variables.items():
            if val == True:
                user_str += (", %s"%var)
        user_str += (")>")

        return user_str

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    word = db.Column(db.String(),nullable=False)
    language = db.Column(db.String(), nullable=False)
    article = db.Column(db.Text())
    video = db.Column(db.Text())
    song = db.Column(db.Text())

    def __repr__(self):
        return "<Word(word='%s', language='%s')>" % (self.word, self.language)