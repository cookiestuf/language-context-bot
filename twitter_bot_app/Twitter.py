from TwitterAPI import TwitterAPI
from twitter_bot_app.db_methods import updateUser, deleteUser
import os
#======== only needed for shell testing 
from dotenv import load_dotenv
load_dotenv()
#========
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', None)

MY_ID_STR = "1235095367600836608"
ACTIONS = set(['subscribe', 'unsubscribe'])
LANGUAGES = set(['spanish'])
def initApiObject():
    
    #user authentication
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)    
    
    return api				
 
def processNewTweetFromOther(eventObj, testing=False):
    """
    Check that it's not a tweet from the app account and extract a word of the day from the Tweet.
    Returns (language, word).
    """
    pass

def processNewTweetAtSelf(eventObj,testing=False):
    """
    Parse eventObj and mention Tweet object to extract user and the language(s) and calls subscribe/unsubscribe.
    returns True if database updated
    returns False if database not updated 
    """
    # TODO: add functionality for multiple languages in one tweet
    tweet_obj = eventObj["tweet_create_events"][0]
    user_mentions = tweet_obj['entities']['user_mentions']
    # a valid user mention is one where there is only 1 user mention object and the id_str matches my id_str
    if len(user_mentions) != 1 and user_mentions[0]['id_str'] != MY_ID_STR:
        print('Tweet does not mention account: %s' % (tweet_obj['text'])) 
        return False
    source_user_id_str = tweet_obj['user']['id_str'] 
    source_user_screen_name = tweet_obj['user']['screen_name'] 
    text= tweet_obj['text'].lower().split(' ')
    language = ""
    action = ""
    for word in text:
        if "@" in word:
            continue
        elif word in ACTIONS:
            action = word
        elif word in LANGUAGES:
            language = word
    if action == "" or language == "":
        print('Tweet is not a valid worded subscription or unsubscription: %s' % (tweet_obj['text']))
        return False
    if action == "subscribe":
        _updateUserLanguages(source_user_id_str, [language], True)
    else:
        _updateUserLanguages(source_user_id_str, [language], False)
    if not testing:
        # TODO: send confirmation tweet to user 
        _postTweet(source_user_screen_name, "confirmed!")
    return True
def _sendUpdateToUsersForLanguage(language):
    """
    Tweets at all subscribed users for language the new word with a link to it used in context.
    """
    return
def _updateUserLanguages(id_str, languages, value):
    """
    Adds or removes languages to user to the database based on value.
    TODO: Sends word of the day if word of the day for language has already been sent out.
    """ 
    # construct dictionary of each language in languages = value
    dictionary = {language: value for language in languages}
    updateUser(id_str, **dictionary)
    return
def _postTweet(screen_name, content):
    """
    Posts a tweet with content and mentions user
    """
    twitterAPI = initApiObject()
    r = twitterAPI.request('statuses/update', {'status': "@%s %s" % (screen_name, content)})
    if r.status_code == 200:
        print('SUCCESS')
        return True
    else:
        print('PROBLEM: ' + r.text) 
        return False
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