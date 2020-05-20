Twitter Bot Technical Spec
Author: Sarah

## Overview
The idea is to create a Twitter Bot that helps its followers learn a word in a specified language in some sort of context a custom number of times a week. This is a medium-sized project that will take roughly 10-15 hr planning, 40-50 hours for the MVP, 8-10hrs testing infrastructure.
-  4/4 - 3 hours updating spec/reading twitter API
- 18/04 - 4 hours updating spec/reading twitter API
- 20/04 - 10:30 - 12:30 starting TDD for basic database methods
- 15/05 - 30 mins: more planning

This will be a python Flask app that will be hosted on Heroku and using PostgresDB with SQLAlchemy and the ORM. 

## helpful references
Customer engagement through DMs: https://developer.twitter.com/en/docs/tutorials/customer-engagement-application-playbook
Another tutorial perhaps: https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/

## Goals & Product Requirements
MVP:
- Allow users to choose language
- send word + context to user 2x wk on Wed and Sun

- strech goals:
a. user chooses their level of the language (tbh beginners shouldn't use this)
b. user can choose context (video, article, song)
c. user can customize which days to receive the link
- future development: i'd like to get some practice with REST APIs at some point and i can basically make these method functions into a java microservice and have my twitter bot ping the microservice and then communicate to twitter, so that's good in the hood. But first, i'll write it at is, then refactor into a microservice! so i won't be overwhelmed by all the things I need to figure out
    /english/date/{word,link}

## Timeline:
There's 3 main chunks to implement:
1. Twitter communication
2. DB connections
3. finding a link to an article to the word


## Methods
global const:
- LANG: [] avail langs
- KNOWN_FOLLOWERS: set() user_ids
[x] create_database(db_name="app"):
1. create user table: cols = username (str), subscribed (0/1), language(0/1) for each language, extra: mon, tues, wed, thurs, fri, sat, sun (days of week are 0/1 values)
2. create word table: cols = language (str), word(str), link(href) extra: article(str), video(str), song(str)

[ ] update_DB(db_name="app",table, data):
- db_name for testing purposes
- makes sure data is in the right format for table
    if table == user
    username, subscribed, language = data
    make sure language is in valid languages
- add data to table

[ ] add_user(user): (maybe not necessary)
when user follows account send msg and update db ( but no language! remind until language set.)
- if user already in DB: do nothing?
- if new user:
1. DM WELCOME + HELP to USER
2. update_db(user_table, [user, 0, None])

[ ] add_language(user, lang):
user subscribes to a language. send msgs and update DB
- call send_message(user, msg_type=TWEET_LANG_SUB_ACK)
- if new user:
    - call send_message(user, msg_type=DM_WELCOME,DM_HELP)
- update_db(user_table,[user, 1, lang])

[ ] unsubscribe (language):
1. remove USER, LANGUAGE from DB

[ ] get_word_of_day(language):
1. 
[ ] get_user_for_language(language):
returns lst of userids subscribed to language

[ ] parse_tweet(msg)
regex parsing to figure out: user, user's desired action & language, call appropiate functions
    if msg == sub:
        subcribe(user,language)
    elif msg == unsub: 
        unsubscribe(user, language)
    else: error handling
- get language: error handling

[ ] get_new_mentions() --> use Account API 
- ~pings mentions timeline every X amt of minutes to see if there are new mentions~
- subscribe to at mentions 
- calls parse_tweet for each mention

[ ] get_followers()
- pings followers and if len(followers) > len(KNOWN_FOLLOWERS):
call new_follower(get_user_object(user_id)) for each new user_id 

[ ] send_message(user, msg_type)
- could be: tweet or DM
- msg_typs:
    - TWEET_LANG_SUB_ACK: "Thank you for subscribing to the word of the day in %s @%s", (LANG, USER_HANDLE)
    - TWEET_LANG_SUB_REM: "You are now unscribed from the word of the day in  %s @%s", (LANG, USER_HANDLE)
    - TWEET_ACTION_ERROR: Sorry! I didn't understand that. Please check your DMs.
    - TWEET_LANG_ERROR: Sorry! That language is not available. Please check your DMs.
    - DM_WELCOME: Hello! Thanks for subscribing to Twitter Bot! I bet you're here to learn another language! Wonderful! My goal is to support you by sending you a word with a link with word used in context. If you haven't already done so, please send me a tweet to subscribe to a language. Languages available: LANG.
    - DM_COMMENTS: You can send me any comments through direct message, but you cannot sub/unsub through DMs.
    - DM_HELP: Here are the available languages: LANG and here are the tweets I understand:
    To subscribe to one language: 
    @bot Subscribe English
    Repeat this process to subscribe to other languages.

    To unsubscribe to one language:
    @bot Unsubscribe English
    Repeat this process to unsubscribe to other languages.




______________________Sample convo____________________________
BOT TO USER---------------
Hello! Thanks for subscribing to Twitter Bot! I bet you're here to learn another language! Wonderful! My goal is to support you by sending you a word with a link with word used in context. The media you receive will be either an article, song, or video. You can customize how often you want to receive words. Here are the available commands:
> change language
> change frequency
> send comment (tell me something!)
> help
> word of the day (to get the word not on schedule)
> cancel
The default is Spanish and receiving links every Wednesday and Saturday. Please type "change language" and "change frequency" to change the default.
USER TO BOT---------------
change language
BOT TO USER---------------
What languages do you want to learn? Available languages are: English, Spanish
USER TO BOT---------------
> English | Spanish | anything else (don't accept and prompt again)
BOT TO USER (prompt again)---------------
Sorry! I didn't understand that. Please send me one of these options: OPTIONS
BOT TO USER (accepted response)---------------
Great! You will receive words in context in LANGUAGE. 
--new message--
How often do you want to receive the links? Here is the default schedule for different levels of language learners:
casual: Monday
inbetween: Wednesday, Saturday
dedicated: Tuesday, Thursday, Sunday
daily: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
custom: you choose!

Please send one of these options: casual, inbetween, dedicated, daily, or custom.
USER TO BOT---------------
some valid options
BOT TO USER-------
some ACK

_______________________End of sample convo______________________

## Testing
make sure to noop/containerize tests
[db_tests]
- create test Db
- update_db try with both user table and word table and diff types of info
- need to clean_data JIC 
- ensure entry is there
- remove_entry()
- ensure it's empty
- destroy DB
[interaction_tests]
- create test_DB with tables
- parse_tweet(msg) with diff inputs (sub, unsub, random, unsub/sub mispelling/unavailable language)
- check that added to test_DB
- test sending DM with link to word of the day for each user in test_DB (noop!)
- delete test_DB
## Operations
logs ALL interactions of bots & users. to add later
