from TwitterAPI import TwitterAPI

import os

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', None)

def initApiObject():
    
    #user authentication
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)    
    
    return api				
 
def processCreateEventTweet(eventObj):
    """
    Check that it's not a tweet from the app account and extract a word of the day from the Tweet.
    Returns (language, word).
    """

def processCreateEventMention(eventObj):
    """
    Parse eventObj and mention Tweet object to extract user and the language(s) and calls subscribe/unsubscribe.
    """

def _updateUsers(language):
    """
    Tweets at all subscribed users for language the new word with a link to it used in context.
    """
def _subscribe(user, languages):
    """
    Adds language to user to the database. Sends word of the day if word of the day for language has already been sent out.
    """ 
def _unsubscribe(user, languages)
    """
    Removes language from user from the database.
    """
def _sendTweet(user, content):
    """
    Tweets content at the user
    """

def processDirectMessageEvent(eventObj):
    
    messageText = eventObj.get('message_data').get('text')
    userID = eventObj.get('sender_id')

    twitterAPI = initApiObject()
            
    messageReplyJson = '{"event":{"type":"message_create","message_create":{"target":{"recipient_id":"' + userID + '"},"message_data":{"text":"Hello World!"}}}}'


    r = twitterAPI.request('direct_messages/events/new', messageReplyJson)
          
    return None      

def processLikeEvent(eventObj):
    userHandle = eventObj.get('user', {}).get('screen_name')
    
    print ('This user liked one of your tweets: %s' % userHandle) 
    
    return None           