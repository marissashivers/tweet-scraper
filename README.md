# tweet-scraper
A Python script that scrapes the Twitter stream and puts the tweets into a MongoDB database. 

## Description
This small application written in Python combines the use of the Twitter API with using a MongoDB database. It was written as an exercise to become familiar with combining these elements into a Python application. It uses two Python libraries, [Tweepy](https://github.com/tweepy/tweepy) and [PyMongo](https://github.com/mongodb/mongo-python-driver).

The application itself listens to Twitter's live stream of tweets, and when your search term is found in a tweet, the program prints the tweet to the terminal, and adds the tweet to your MongoDB database with the following format:
```
{
  'username': username of account tweeting,
  'tweet': the tweet itself 
}
```

## How to use
You will first need to install both Tweepy and PyMongo, as well as install MongoDB on your computer. You will also need to have a [Twitter developer account](https://developer.twitter.com/) and obtain credentials to access the Twitter API. 

Before you run the program, you will need to replace a few placeholders within the code with your own information. First, create a MongoDB database and collection, locate within the code 'YOUR_DATABASE_NAME' and 'YOUR_COLLECTION_NAME', and replace them with your own respective database and collection names.

Next, replace the placeholders for your Twitter credentials (consumer_key, consumer_secret, access_token, and access_token_secret) and replace them accordingly.

Finally, you are ready to run the program. Note that while the program is currently written to search for all Tweets containing the phrase 'SQL injection', you can easily modify this to whichever search term(s) you would like. Simply change the search term within this block of code, found in the last two lines of the pgoram:
```
# Search for all tweets containing the keyword 'sql injection'
myStream.filter(track=['sql injection'], is_async=True)
```
