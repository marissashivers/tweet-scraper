# Using Tweepy with Twitter's API
# Using pymongo
from pymongo import MongoClient
import tweepy

myclient = MongoClient()
myclient = MongoClient("mongodb://localhost:27017/")

# Navigate to proper database and collection
# Replace 'YOUR_DATABASE_NAME' with the name of your MongoDB database
# Replace 'YOUR_COLLECTION'_NAME' with the name of your MongoDB collection
mydb = myclient['YOUR_DATABASE_NAME']
mycol = mydb['YOUR_COLLECTION_NAME']

##################################################
consumer_key = "YOUR_API_KEY" # Replace with your consumer API key
consumer_secret = "YOUR_API_SECRET_KEY" # Replace with your consumer API secret key
access_token = "YOUR_ACCESS_TOKEN" # Replace with your access token
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET" # Replace with your access token secret

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
API = tweepy.API(auth)

##################################################

# Listening to a live stream of Tweets
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		# Print the tweet
		print('{} says: {}'.format(status.user.screen_name, status.text))
		# Add the tweet to the MongoDB database
		dict = { 'username': status.user.screen_name, 'tweet': status.text }
		mycol.insert_one(dict)
		print()
	def on_error(self, status_code):
		print (status_code)
	
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = API.auth, listener=myStreamListener)

# Search for all tweets containing the keyword 'sql injection'
myStream.filter(track=['sql injection'], is_async=True)

