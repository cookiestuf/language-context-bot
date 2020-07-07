import pytest
from twitter_bot_app.models import User, Word
from twitter_bot_app import db
from twitter_bot_app.Twitter import processNewTweetAtSelf, processNewTweetFromOther
from twitter_bot_app.db_methods import deleteUser

my_user_id = "12345678"
my_screen_name = "emdicsarah"
def test_processNewTweetFromOther(app):
    return 
def test_processNewTweetAtSelfSubscribe(app):
    new_user_id_str = "944480690"
    new_user_screen_name = "spanishsubscriptor"
    # check that db has correct subscribed entry for json
    tweet_dict = {"created_at": "Thu May 10 17:41:57 +0000 2018",
	"id_str": "994633657141813248",
	"text": "@%s subscribe spanish" % my_screen_name,
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
      "id_str": my_user_id
    }],}
}
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
    json = '{ "for_user_id": my_user_id,	"tweet_create_events": [  {	<Tweet Object>}]}'

    # check that db has correct unsubscribed entry for json

# TODO: add test to check that the correct process event is called