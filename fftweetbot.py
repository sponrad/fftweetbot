#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
query = "bullsnation"
max_tweets = 1

for tweet in tweepy.Cursor(api.search,
                           q=query,
                           rpp=5,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items(max_tweets):
    #print tweet.id, tweet.created_at, tweet.text
    #print tweet.author, tweet.user
    
    #api.create_favorite(tweet.id)

    #api.send_direct_message(user_id=tweet.user.id, text="YO DOG check me out!")

    """ Need to figure out what I want this bot to accomplish """
    """ given a list of search terms do something """


#api.send_direct_message(user="username", text="YO DOG check me out!")



