import argparse
from configparser import ConfigParser
from utils import *

if __name__ == "__main__":

    # parameters to get the tweet id
    parser = argparse.ArgumentParser()
    parser.add_argument("--tweet_id", help="path where to save the files")
    args = parser.parse_args()
    tweet_id = int(args.tweet_id)

    # loading key from the config ini
    configur = ConfigParser(interpolation=None)
    configur.read('config.ini')

    bearer = configur.get("keys", "bearer")

    headers = {"Authorization": "Bearer {}".format(bearer)}

    # let's collect the conversation id for the tweet of interest
    r = get_request(f"https://api.twitter.com/2/tweets?ids={tweet_id}&tweet.fields=conversation_id", headers=headers)
    conversation_id = r.json()["data"][0]["conversation_id"]

    # some parameters
    query_params = {
        'query': 'conversation_id:{}'.format(conversation_id),
        'tweet.fields': 'conversation_id',
        'start_time': '2021-01-25T00:00:00Z', # <-- super important
        'max_results': 50}

    search_url = "https://api.twitter.com/2/tweets/search/all"

    r = get_request(search_url, headers=headers, params=query_params)

    print(r.json())
