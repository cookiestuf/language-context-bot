import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.Twitter import processNewTweetAtSelf, processNewTweetFromOther
from twitter_bot_app.db_methods import updateUser, deleteUser

my_user_id = "12345678"
my_screen_name = "emdicsarah"
new_user_id_str = "944480690"
new_user_screen_name = "spanishsubscriptor"

# check that db has correct subscribed entry for json
def get_tweet(text):
    return {"created_at": "Thu May 10 17:41:57 +0000 2018",
"id_str": "994633657141813248",
"text": "@%s %s" % (my_screen_name, text),
"user": {
    "id_str": new_user_id_str,
    "screen_name": new_user_screen_name
},
"extended_tweet": {},"entities": {"hashtags": [],
"user_mentions": [{
    "name": "Sarah Zhou",
    "indices": [
    1,
    15
    ],
    "screen_name": my_screen_name,
    "id": int(my_user_id),
    "id_str": my_user_id }],}}

def test_processNewTweetFromOther(app):
    return 
def test_processNewTweetAtSelfSubscribe(app):
    tweet_dict = get_tweet("@emdicsarah subscribe spanish")
    event_obj = {"for_user_id": my_user_id,"tweet_create_events": [tweet_dict]}
    processNewTweetAtSelf(event_obj,testing=True)
    new_user = User.query.filter_by(id_str=new_user_id_str).first()
    assert new_user != None
    assert new_user.id_str == new_user_id_str
    assert new_user.spanish == True
    deleteUser(new_user_id_str)
    new_user = User.query.filter_by(id_str=new_user_id_str).first()
    assert new_user == None

def test_processNewTweetAtSelfUnsubscribe(app):
    tweet_dict = get_tweet("@emdicsarah unsubscribe spanish")
    event_obj = {"for_user_id": my_user_id,"tweet_create_events": [tweet_dict]}
    updateUser(new_user_id_str, spanish=True)
    new_user = User.query.filter_by(id_str=new_user_id_str).first()
    assert new_user.spanish == True

    processNewTweetAtSelf(event_obj,testing=True)
    new_user = User.query.filter_by(id_str=new_user_id_str).first()
    assert new_user.spanish == False
    deleteUser(new_user_id_str)
    new_user = User.query.filter_by(id_str=new_user_id_str).first()
    assert new_user == None

# TODO: add test to check that the correct process event is called