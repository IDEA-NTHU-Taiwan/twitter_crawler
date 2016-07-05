# A simple crawler which stores to a mongoDB
import requests
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient

# Connection to Mongo Database
client = MongoClient("localhost", 27017)
db = 'NAME_OF_DATABASE'
collection = 'NAME_OF_COLLECTION'

# Consumer Key
ckey = 'YOUR_CONSUMER_KEY'
# Consumer Secret
csecret = 'YOUR_CONSUMER_SECRET'
# Access Token
atoken = 'YOUR_ACCESS_TOKEN'
# Acces Secret
asecret = 'YOUR_ACCESS_SECRET'

# write tweet to db
def post_tweet_to_db(tweet):
  post = {"tweet": tweet}
  collection.insert(post)
  return True  

# Stream Listener
class listener(StreamListener):
  def on_data(self, data):
    try:
      # TODO: pick what you want to store from the response
      reponse = json.loads(data)
      tweet = reponse['text']

      # uncomment next line to insert tweet information into database or write to file
      #post_tweet_to_db(tweet)
      print (tweet)

    except Exception:
      return True

  def on_error(self, status):
    print (status)
    return True
    return False

  def on_timeout(self):
    print >> sys.stderr, 'Timeout...'
    return True # Don't kill the stream
    return False

  def on_status(self, status):
    print (status.text)

# Starts streaming
while True:
  try:
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    track = ['#joy','#sad',] #Keyword to track (you can provide multiple keywords separated by a comma)
    twitterStream.filter(track=track)
  except:
    continue