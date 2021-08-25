import tweepy
from datetime import datetime
import json


class StreamingCollectorListener(tweepy.StreamListener):
    def __init__(self, file_path, n_tweets):
        super().__init__()
        file_name = str(datetime.date(datetime.now()))

        self.trends_counter = 0
        self.n_tweets = n_tweets
        self.opened_file = open(file_path+'data/'+file_name, "w")

    def on_status(self, status):
        if self.trends_counter == self.n_tweets:
            self.opened_file.close()
            exit()

        if not status.retweeted and 'RT @' not in status.text:
            self.trends_counter = self.trends_counter + 1
            self.opened_file.write(json.dumps(status._json) + "\n")
            self.opened_file.flush()
