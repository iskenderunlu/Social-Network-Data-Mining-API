from __future__ import unicode_literals
import tweepy
import json
from json import dumps
from flask import Flask, jsonify, Response, make_response
#from flask.ext.responses import json_response, xml_response, auto_response
from werkzeug.exceptions import default_exceptions 
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route("/<screen_name>/<maxnumtweets>/<numtweetsbystep>",  methods=['GET'])
def get_all_tweets(screen_name,maxnumtweets,numtweetsbystep):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	consumer_key='3uVVgZoOq3WrCMJNL5WMIx2AP'
	consumer_secret='q6JV9QKe9rEKhHx7xAgR6zpQdSoLyrCw0pfb5jT3l5iEuLLNSv'
	access_key='2906391365-VEAnfVxOR0cPtAfrPYvkuagKhkYpXb6fCP9inDZ'
	access_secret='Bm7RDc9xMr95LPZjKJKd3BN7sYaz3CF3STR81jdwpi0T5'
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count = numtweetsbystep)
	

	#save most recent tweets
	alltweets.extend(new_tweets)
	string_form_alltweets=[]
	maxnumtweets=int(maxnumtweets)
	maxforbreak=int(maxnumtweets)
	numtweetsbystep=int(numtweetsbystep)
	if numtweetsbystep == maxnumtweets :
		
		for x in xrange(len(alltweets)):
			string_form_alltweets.append(str(alltweets[x]))
			if x == maxnumtweets:
				break
				
			print x
			pass
		return jsonify(results=string_form_alltweets)

	elif (maxnumtweets >= numtweetsbystep) and (maxnumtweets % numtweetsbystep == 0):
		#save the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		print maxnumtweets
		#keep grabbing tweets until there are no tweets left to grab
		maxnumtweets-=numtweetsbystep
		while (len(new_tweets) > 0) and (maxnumtweets >0):
			print "getting tweets before %s" % (oldest)
			
				
			#all subsiquent requests use the max_id param to prevent duplicates
			new_tweets = api.user_timeline(screen_name = screen_name,count = numtweetsbystep,max_id = oldest)
			maxnumtweets -=numtweetsbystep 
			#save most recent tweets

			alltweets.extend(new_tweets)

			
			# update the id of the oldest tweet less one
			oldest = alltweets[-1].id - 1
			
			#print "...%s tweets downloaded so far" % (len(alltweets))

		for x in xrange(len(alltweets)):
			string_form_alltweets.append(str(alltweets[x]))
			if x == maxforbreak:
				break
			print x
			pass

	  	return jsonify(results=string_form_alltweets)
	#transform the tweepy tweets into a 2D array that will populate the csv	
	#outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	#with open('%s_tweets.csv' % screen_name, 'wb') as f:
	#	writer = csv.writer(f)
	#	writer.writerow(["id","created_at","text"])
	#	writer.writerows(outtweets)
	
	#pass

if __name__ == '__main__':
	app.debug=True
	app.run(host="0.0.0.0")
