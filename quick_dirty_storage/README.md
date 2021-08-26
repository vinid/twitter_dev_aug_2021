# Streaming directly into MongoDB

![](../img/part_2.png)

## Requirements

You need tweepy and [PyMongo](https://pymongo.readthedocs.io/en/stable/) installed on your machine.
You also need a [MongoDB](https://www.mongodb.com/) instance that is up and running.

## Running

General command to run is the following

    python3 collect.py \
        --mongo_db desired_mongodb_database \
        --mongo_collection desired_mongodb_collection \
        --keyword cat
        
where --keyword allows you to select a keyword of interest

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