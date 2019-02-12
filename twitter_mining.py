import json
import operator
import re
import string
from collections import Counter, defaultdict

import tweepy
from tweepy import OAuthHandler

#Using OAuth interface to authorize our app to access Twitter
consumer_key = "B6wxuQ1SskuGQd36OtxJ2muyb"
consumer_secret = "fNTJpe9aXDBnQz0sFyvEkmBcN2AbMXPEg6Bwdk6FRpujLRX8pn"
access_token = "4274018593-WhYql5iMDg8HAoTevROut6nT7CH3X7MfjDfdAOu"
access_secret = "OnAL6UANa132KMLfpsDM2XJTcdEOkSB4yrG9NtWDs7IqZ"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# The api variable is now our entry point for most of the operations we can perform with Twitter.
api = tweepy.API(auth)

#To continuously gather tweets about a topic or #hashtag we use streaming API StreamListener()
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('info.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=["#nike","#addidas","#rebook","#skechers","#puma"])
