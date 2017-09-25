# Twitter Tweet Fetching by parameters in Jason Format

I am using hadoop python implementations. Today, You can fetch tweets according to some parameters using Twitter Restful APIs. You need to obtain credentials of Twitter APIs(OAuth access token on behalf of a Twitter use) to work with the API like below:

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
