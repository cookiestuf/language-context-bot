import functools

from flask import Blueprint, current_app,Flask, request, render_template, send_from_directory, make_response
from http import HTTPStatus
from twitter_bot_app.db_methods import updateUser, deleteUser
import hashlib, hmac, base64, os, logging, json

CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
CURRENT_USER_ID = os.environ.get('TWITTER_CURRENT_USER_ID', None)
	     
from twitter_bot_app import db
from twitter_bot_app.models import User, Word
from twitter_bot_app.Twitter import processNewTweetAtSelf
bp = Blueprint('twitter_conn', __name__)
MY_USER_ID="1235095367600836608"
"""
File written by @RickRedSix with edits by Sarah
"""
@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        #current_app.logger.debug('this is a DEBUG message')
        #current_app.logger.info("hello and welcome to %s" % current_app)
        #current_app.logger.warning('this is a WARNING message')
        #current_app.logger.error('this is an ERROR message')
        #current_app.logger.critical('this is a CRITICAL message')
        return render_template('index.html')

#The GET method for webhook should be used for the CRC check
#TODO: add header validation (compare_digest https://docs.python.org/3.6/library/hmac.html)
@bp.route('/webhook', methods=('GET', 'POST'))
def webhook():
    if request.method == 'GET':
        #twitterCrcValidation
        
        crc = request.args['crc_token']
    
        validation = hmac.new(
            key=bytes(CONSUMER_SECRET, 'utf-8'),
            msg=bytes(crc, 'utf-8'),
            digestmod = hashlib.sha256
        )
        digested = base64.b64encode(validation.digest())
        response = {
            'response_token': 'sha256=' + format(str(digested)[2:-1])
        }
        print('responding to CRC call')

        return json.dumps(response)   
    elif request.method == 'POST':
#The POST method for webhook should be used for all other API events
#TODO: add event-specific behaviours beyond Tweet and Like (such as Direct message)
        #twitterEventReceived():
	  		
        requestJson = request.get_json()

        #dump to logging for debugging purposes
        current_app.logger.info(json.dumps(requestJson, indent=4, sort_keys=True))   
        keys = requestJson.keys()
        if 'favorite_events' in keys:
            tweet_obj = requestJson['favorite_events'][0].get("favorited_status")
            user_obj = tweet_obj.get("user") # user that did the favoriting ie me
            current_app.logger.info("You just favorited %s\'s tweet \"%s\"" % (user_obj.get("screen_name"), tweet_obj.get("text")))
            new_user = updateUser(user_obj.get("id_str"))
            current_app.logger.info(user_obj.get("id_str"))
        elif 'tweet_create_events' in keys: 
            if requestJson["for_user_id"] == MY_USER_ID:
                processNewTweetAtSelf(requestJson)
        else:
            #Event type not supported
            return ('', HTTPStatus.OK)

    return ('', HTTPStatus.OK)
