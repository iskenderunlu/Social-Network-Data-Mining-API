# -*- coding: utf-8 -*-
#imports
import hadoopy
from slistener import SListener
import time, tweepy, sys
from tweepy.api import API
from tweepy import auth 
import json
import streaming
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os 
import stat
from tweepy import auth


##  authentication
#username = 'UnluIskender' ## put a valid Twitter username here

consumer_key = '3uVVgZoOq3WrCMJNL5WMIx2AP'
consumer_secret = 'q6JV9QKe9rEKhHx7xAgR6zpQdSoLyrCw0pfb5jT3l5iEuLLNSv'
access_token = '2906391365-VEAnfVxOR0cPtAfrPYvkuagKhkYpXb6fCP9inDZ'
access_secret = 'Bm7RDc9xMr95LPZjKJKd3BN7sYaz3CF3STR81jdwpi0T5'

#auth     = tweepy.auth.BasicAuthHandler(username, password)
#auth     = get_xauth_access_token(username, password)
#auth    =   OAuthHandler(consumer_key, consumer_secret)
#api      = tweepy.API(auth)
# initialize blank list to contain tweets

class TweetListener(StreamListener):
# A listener handles tweets are the received from the stream.
# This is a basic listener that just prints received tweets to standard output
    def on_data(self, data):
        print (data)
        
        return True
    def on_error(self, status):
        print (status)


try:
    f=open(hdfs.txt, 'a')
    f.close()
except BaseException as e:
    print("Error on_data: %s" % str(e))
    time.sleep(5)

tweets = []
class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.save_file = tweets

    def on_data(self, tweet):
        self.save_file.append(json.loads(tweet))
        print tweet
        save_file.write(str(tweet))


def main():
        
 
    #listen = SListener(api, 'myprefix')
    #stream = tweepy.Stream(auth, listen)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, TweetListener())
    stream.filter(track=['nba'])

    api = tweepy.API(auth)
 
    auth.set_access_token(access_token, access_secret)
    twitterStream = Stream(auth,TweetListener())

    #hadoop fs -put twitterStream /tweepy/hdfs.txt
    #os.system('echo "%s" | hadoop fs -put twitterStream /tweepy/hdfs.txt' %(json.dump(twitterStream)))



    print ("Streaming started...")

    try: 
        stream.filter(track = track)
    except:
        print ("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()
