import tweepy
from datetime import datetime
import json


class StreamingCollectorListener(tweepy.StreamListener):
    """
    Extends the basic stream listener
    """
    def __init__(self, file_path, n_tweets):
        """

        :param file_path: folder in which we want to save the daily tweets
        :param n_tweets: maximum number of tweets to collect
        """
        super().__init__()
        file_name = str(datetime.date(datetime.now()))

        self.n_tweets = n_tweets
        self.opened_file = open(file_path + "/" + file_name, "w")

    def on_status(self, status):
        if self.trends_counter == self.n_tweets:
            self.opened_file.close()
            return False

        if not status.retweeted and 'RT @' not in status.text:

            self.trends_counter = self.trends_counter + 1
            self.opened_file.write(json.dumps(status._json) + "\n")
            self.opened_file.flush()
