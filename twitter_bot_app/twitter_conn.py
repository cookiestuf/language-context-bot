import functools

from flask import Blueprint, Flask, request, send_from_directory, make_response
from http import HTTPStatus

import hashlib, hmac, base64, os, logging, json

CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
CURRENT_USER_ID = os.environ.get('TWITTER_CURRENT_USER_ID', None)
	     
app = Flask(__name__)	

from twitter_bot_app import db
from twitter_bot_app.models import User, Word

bp = Blueprint('twitter_conn', __name__)
"""
File written by @RickRedSix with edits by Sarah
"""
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
#TODO: add event-specific behaviours beyond Direct Message and Like
        #twitterEventReceived():
	  		
        requestJson = request.get_json()

        #dump to console for debugging purposes
        print(json.dumps(requestJson, indent=4, sort_keys=True))
                
        if 'direct_message_events' in requestJson.keys():
            # DM recieved, process that
            eventType = requestJson['direct_message_events'][0].get("type")
            messageObject = requestJson['direct_message_events'][0].get('message_create', {})
            messageSenderId = messageObject.get('sender_id')   
                
            #message is from myself so ignore (Message create fires when you send a DM too)   
            if messageSenderId == CURRENT_USER_ID:
                return ('', HTTPStatus.OK)
            from . import Twitter
            Twitter.processDirectMessageEvent(messageObject)    
                    
        else:
            #Event type not supported
            return ('', HTTPStatus.OK)
    
    return ('', HTTPStatus.OK)