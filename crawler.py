# A simple crawler which stores to a mongoDB
import sys, json, config
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient

KEYWORDS = ['a', 'the', 'and']  # Keyword to track (you can provide multiple keywords separated by a comma)
LANGUAGES = ['en']
WANTED_KEYS = [
    'id_str',
    'text',
    'created_at',
    'in_reply_to_status_id_str',
    'in_reply_to_user_id_str']  # Wanted keys to store in the database

# Connection to Mongo Database
client = MongoClient(config.MONGODB['hostname'], config.MONGODB['port'])
db = client[config.MONGODB['db']]
collection = db[config.MONGODB['collection']]


# write tweet to db
def post_tweet_to_db(tweet):
    post = {"tweet": tweet}
    collection.insert(post)
    return True


# Stream Listener
class Listener(StreamListener):

    @staticmethod
    def on_data(data):
        try:
            reponse = json.loads(data)
            tweet = {key: reponse[key] for key in set(WANTED_KEYS) & set(reponse.keys())}

            # uncomment next line to insert tweet information into database or write to file
            # post_tweet_to_db(tweet)
            print(tweet)

        except Exception:
            return True

    @staticmethod
    def on_error(status):
        print (status)
        return True

    @staticmethod
    def on_timeout():
        print >> sys.stderr, 'Timeout...'
        return True  # Don't kill the stream

    @staticmethod
    def on_status(status):
        print (status.text)

# Starts streaming
while True:
    try:
        auth = OAuthHandler(
            config.TWEETER['consumer_key'], config.TWEETER['consumer_secret'])
        auth.set_access_token(
            config.TWEETER['access_token'], config.TWEETER['access_secret'])
        twitterStream = Stream(auth, Listener())
        twitterStream.filter(languages=LANGUAGES, track=KEYWORDS)
    except KeyboardInterrupt:
        print("Bye")
        sys.exit()
