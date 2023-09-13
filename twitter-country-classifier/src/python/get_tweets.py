from datetime import datetime
import secret_config as conf
import tweepy
import json
import sys
import re

# API keys stored in 'secret_config.py',
# follow format found in 'example_secret_config.py'
consumer_key = conf.consumer_key
consumer_secret_key = conf.consumer_secret_key

access_token = conf.access_token
access_token_secret = conf.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# [ SW_corner_long , SW_corner_lat , NE_corner_long , NE_corner_lat ]
ENGLAND = [-4.819226, 50.132493, 1.545378, 54.684025]
WEST_US = [-124.329638, 31.951539, -84.120843, 45.283106]
EAST_US = [-79.294871, 32.851545, -69.346595, 42.941889]

# NOTE: Remember to change 'location=' in my_stream.filter when changing the COUNTRY
# so that they match (ENGLAND -> ENGLAND; WEST_US,EAST_US -> AMERICA)
COUNTRY = 'ENGLAND'
LIMIT = 2340

out = open(f'../data/{COUNTRY}.txt', 'a', encoding='utf8')

i, limit = 1, LIMIT

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        global i
        global limit

        if tweet._json['lang'] != 'en':
            pass
         
        else:
            text = tweet._json['text']
            text = re.sub(r'\n', ' ', text)
            text = re.sub(r',', '', text)

            out.write(f"{COUNTRY},{text}")
            out.write('\n')
            print(f"[ {datetime.now().strftime('%H:%M.%S')} ] [ {i} ] tweet written")
            
            i += 1

            if i >= limit:
                sys.exit(0)

    def on_error(self, status_code):
        if status_code == 402:
            return False


my_streamer = MyStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=my_streamer)

# east not done yet
my_stream.filter(locations=ENGLAND)

out.close()