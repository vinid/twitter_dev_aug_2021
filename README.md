# Twitter Developer Platform: Using Twitter APIs for Academic Research

All the scripts require a config.ini file in which the keys are put. There is a task-specific readme in 
every folder.

## Part I - Building a Representative Dataset of a Location/Language

**Use Case**: When there's the need to collect data in a specific language to build a dataset that is somewhat
representative. We don't want to track keywords. Instead, we can collect trending topics for a place and track those.

## Part II - Quick and Dirty Storage with MongoDB

**Use Case**: When there's the need to put up a quick streaming pipeline to track some keywords and
tho store them somewhere safe without thinking too much. [MongoDB]() is a good solution because set up
should be easy and python has a great integration with it thanks to [PyMongo]().

## Part III - Reconstructing Conversations on Twitter

**Use Case**: This just showcases how to reconstruct conversations given a single Tweet Id.