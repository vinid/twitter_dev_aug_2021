import tweepy
from pymongo import MongoClient

class MongoDBCollectorListener(tweepy.StreamListener):
    """
    Extends the basic stream listener and adds a call to MongoDB
    """
    def __init__(self, database, collection):
        """

        :param database: MongoDB database name
        :param collection: MongoDB collection name
        """
        super().__init__()
        client = MongoClient()
        self.db = client[database][collection]

    def on_status(self, status):

        if not status.retweeted and 'RT @' not in status.text:
            self.db.insert(status._json)
