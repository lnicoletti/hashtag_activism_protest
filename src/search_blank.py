import tweepy 
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
import time
import datetime
from twitter_miner import *

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

text_list = [] 
hashtag_list = []
mentions_list = []
from_list = []
to_list = []

full_list = text_list
full_list.extend(hashtag_list)
full_list.extend(mentions_list)
full_list.extend(from_list)
full_list.extend(to_list)

credentials = Credentials(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)

file_name_base = '' #enter path where you want the file saved to

mine_tweets(credentials, full_list, file_name_base)


 
