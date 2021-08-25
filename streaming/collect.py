import tweepy
from configparser import ConfigParser
from streaming.streaming_collector import StreamingCollectorListener
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--save_path", help="path where to save the files")
parser.add_argument("--trending_location", help="woeid to track")
parser.add_argument("--n_tweets", help="number of tweets to collect")
parser.add_argument("--config_path", help="location of the config file")
parser.add_argument("--language", help="language")

args = parser.parse_args()
save_path = args.save_path
location = args.trending_location
n_tweets = args.n_tweets
config_path = args.config_path
language = args.language

configur = ConfigParser()
configur.read('config.ini')

consumer_key = configur.get("keys", "consumer_key")
consumer_secret = configur.get("keys", "consumer_secret")
access_token = configur.get("keys", "access_token")
access_token_secret = configur.get("keys", "access_token_secret")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


collected_trends = api.trends_place(location) # from the end of your code
data = collected_trends[0]
trends = data['trends']
all_the_trends = [trend['name'] for trend in trends]

myStreamListener = StreamingCollectorListener(save_path, n_tweets)
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=all_the_trends, languages=[language])