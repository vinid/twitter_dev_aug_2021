# Building a Representative Dataset

![](../img/part_1.png)

## Requirements

You just need tweepy installed to run this script. 

## Running

    python3 collect.py \
           --save_path save_data  \
           --trending_location 23424853  \
           --language it  \
           --n_tweets 2 

`23424853` is the WOEID code of Italy. 

## Config File

You need to have a config.ini file, somewhere on your machine where to store the API keys. You can
pass the location of the config.ini to the script, default location is the folder from where you
run the script.
```
[keys]
consumer_key = something
consumer_secret = something
access_token = something
access_token_secret = something
```