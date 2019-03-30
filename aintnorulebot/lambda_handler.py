import os
import random
from typing import List

import tweepy

ANIMALS = [
    'Dog',
    'Cat',
    'Raccoon',
]

SPORTS = [
    'Basketball',
    'Football',
    'Tennis',
    'Rugby',
]


def post_tweet(event, context):
    client = get_twitter_client_from_environment()
    message = get_tweet_message(ANIMALS, SPORTS)

    print(f"Posting: {message} to twitter")
    client.update_status(message)

    return {'message': message}


def get_tweet_message(animals: List[str], sports: List[str]) -> str:
    animal = random.choice(animals)
    sport = random.choice(sports)
    return f"Ain't no rule that says an {animal} can't play {sport}"


def get_article(noun):
    if len(noun) == 0:
        return 'a'
    pass


def get_twitter_client_from_environment():
    return get_twitter_client(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_key=os.environ['TWITTER_ACCESS_KEY'],
        access_secret=os.environ['TWITTER_ACCESS_SECRET'],
    )


def get_twitter_client(consumer_key, consumer_secret, access_key, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return tweepy.API(auth)


if __name__ == '__main__':
    print("Yo!")
