from dotenv import load_dotenv
import os
import tweepy
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
token_secret = os.getenv("TOKEN_SECRET")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)
print ("Tweet From Terminal")
print ("...................")
tweet = input("What Would You Like To Tweet? ")
api.update_status(status=(tweet))
print ("Done!")