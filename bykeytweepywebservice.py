# -*- coding: utf-8 -*-
#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------
from __future__ import unicode_literals
from twitter import *
import json
from json import dumps
from flask import Flask, jsonify, Response, make_response
#from flask.ext.responses import json_response, xml_response, auto_response
from werkzeug.exceptions import default_exceptions 
from werkzeug.exceptions import HTTPException
from flask import Flask

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------

#@app.route("/<key>/<maxnumtweets>",  methods=['GET'])


app = Flask(__name__)

@app.route("/<key>/",  methods=['GET'])
def search_by_key(key):
	
	config = {}
	execfile("config.py", config)

	#-----------------------------------------------------------------------
	# create twitter API object
	#-----------------------------------------------------------------------
	twitter = Twitter(
			        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


	#-----------------------------------------------------------------------
	# perform a basic search 
	# Twitter API docs:
	# https://dev.twitter.com/docs/api/1/get/search
	#-----------------------------------------------------------------------
	key=str(key)
	query = twitter.search.tweets(q = key)

	#-----------------------------------------------------------------------
	# How long did this query take?
	#-----------------------------------------------------------------------
	#print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

	#-----------------------------------------------------------------------
	# Loop through each of the results, and print its content.
	#-----------------------------------------------------------------------
	#for result in query["statuses"]:
	#	print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])

	#for tweet in query['statuses']:
	#	print tweet
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	alltweets.extend(query['statuses'])
	string_form_alltweets=[]
	for x in xrange(len(alltweets)):
		string_form_alltweets.append(str(alltweets[x]))

				
		print x
		pass
	return jsonify(results=string_form_alltweets)

if __name__ == '__main__':
	app.debug=True
	app.run(host="0.0.0.0")
