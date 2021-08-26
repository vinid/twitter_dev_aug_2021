# Reconstruct a Conversation form a Tweet Id

## Requirements

You just need tweepy installed to run this script. 

## Running

General command to run is the following

    python3 reconstruct.py --tweet_id 1418523644695810051


## Config File

You need to have a config.ini file, somewhere on your machine where to store the API keys. You can
pass the location of the config.ini to the script, default location is the folder from where you
run the script.

```
[keys]
bearer = something
```