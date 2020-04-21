import random
import time
import sqlite3

from typing import List
import requests
from twitter import OAuth, Twitter

import credentials

oauth = OAuth(
        credentials.ACCESS_TOKEN,
        credentials.ACCESS_SECRET,
        credentials.CONSUMER_KEY,
        credentials.CONSUMER_SECRET
    )
t = Twitter(auth=oauth)

##constants
DB_NAME = "app_data"
def create_database(name=DB_NAME):
    """
    Setup a database NAME
    """
    conn = sqlite3.connect("{}.db".format(name))
    cursor = conn.cursor()
    # create a table
    cursor.execute("""CREATE TABLE users 
                        (id text PRIMARY KEY, subscribed int DEFAULT 0, english int DEFAULT 0)
                    """)
    
    conn.commit()
    cursor.execute("""CREATE TABLE words 
                        (language text PRIMARY KEY, word text, link text)
                    """)
    conn.commit()
    cursor.close()
    conn.close()

def update_database(table, data,name=DB_NAME):
    return

def get_users_for_language(language:str, name=DB_NAME) -> List[str]:
    return []

def main():
    """
    it = globals()['scrape_blog']()
    while True:
        try:
            tweet = next(it)
            t.statuses.update(status=tweet)
        except StopIteration:
            return
    """
    
if __name__ == "__main__":
    main()
