import tweepy
from configparser import ConfigParser
from streaming_collector import MongoDBCollectorListener
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--mongo_db", help="path where to save the files")
    parser.add_argument("--mongo_collection", help="woeid to track")
    parser.add_argument("--keyword", help="number of tweets to collect")
    parser.add_argument("--config_path", help="location of the config file", default="config.ini")

    args = parser.parse_args()
    mongo_db = args.mongo_db
    keyword = args.keyword
    mongo_collection = args.mongo_collection

    config_path = args.config_path

    configur = ConfigParser()
    configur.read('config.ini')

    consumer_key = configur.get("keys", "consumer_key")
    consumer_secret = configur.get("keys", "consumer_secret")
    access_token = configur.get("keys", "access_token")
    access_token_secret = configur.get("keys", "access_token_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    print("Streaming")
    myStreamListener = MongoDBCollectorListener(mongo_db, mongo_collection)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(track=[keyword])