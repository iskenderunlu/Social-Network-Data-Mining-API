from __future__ import unicode_literals
import tweepy
import tweepy
import json
from json import dumps
from flask import Flask, jsonify, Response, make_response
from flask.ext.responses import json_response, xml_response, auto_response
from werkzeug.exceptions import default_exceptions 
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
#from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

@app.route("/<screen_name>/<max_tweets>/<query>",  methods=['GET'])
def fetchby_key_username2(screen_name,max_tweets,query):
	# Twitter API credentials
	consumer_key = "3uVVgZoOq3WrCMJNL5WMIx2AP"
	consumer_secret = "q6JV9QKe9rEKhHx7xAgR6zpQdSoLyrCw0pfb5jT3l5iEuLLNSv"
	access_key = "2906391365-VEAnfVxOR0cPtAfrPYvkuagKhkYpXb6fCP9inDZ"
	access_secret = "Bm7RDc9xMr95LPZjKJKd3BN7sYaz3CF3STR81jdwpi0T5"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
	#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)

	

	searched_tweets = [status for status in tweepy.Cursor(api.search, id=screen_name,q=query).items(max_tweets)]


	# [function definition for is_rate_limit_error, cut out for your reading pleasure]
	try:
	    api.do_twitter_things()
	    searched_tweets = [status for status in tweepy.Cursor(api.search, id=screen_name,q=query).items(max_tweets)]
	except tweepy.TweepError as e:
	    if not is_rate_limit_error(e):
	        raise e
	    handle_rate_limit_error()


	# [function definition for is_rate_limit_error, cut out for your reading pleasure]
	try:
	    api.do_twitter_things()
	    searched_tweets = [status for status in tweepy.Cursor(api.search, id=screen_name,q=query).items(max_tweets)]
	    data = api.rate_limit_status()
	    print api.rate_limit_status()
	    print data['resources']['statuses']['/statuses/home_timeline']
	    print data['resources']['users']['/users/lookup']

	except tweepy.TweepError as e:
	    if not is_rate_limit_error(e):
	        raise e
	    handle_rate_limit_error()

	#searched_tweets = [status for status in tweepy.Cursor(api.search, id=screen_name,q=query).items(max_tweets)]

	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	#count=0
	#for tweet in searched_tweets:
	#	print tweet
	#	count+=1
	#	print count

	#save most recent tweets
	alltweets.extend(searched_tweets)
	string_form_alltweets=[]
	maxnumtweets=int(max_tweets)
	maxforbreak=int(max_tweets)
	


	for x in xrange(len(alltweets)):
			string_form_alltweets.append(str(alltweets[x]))
			if x == maxnumtweets:
				break
				
			print x
			pass

    
	return jsonify(results=string_form_alltweets)

if __name__ == '__main__':
	app.debug=True
	app.run()
