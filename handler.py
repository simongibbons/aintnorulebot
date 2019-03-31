import os
import random
from typing import List

import tweepy

ANIMALS = [
    'Dog',
    'Cat',
    'Raccoon',
    'Manatee',
    'Shark',
    'Tiger',
    'Hawk',
    'Rattlesnake',
    'Moose',
    'Mongoose',
    'Lion',
    'Giraffe',
    'Panda',
    'Capybara',
]

SPORTS = [
    'Basketball',
    'Football',
    'Tennis',
    'Rugby',
    'Water Polo',
    'Lacrosse',
    'Curling',
    'Golf',
    'Ultimate Frisbee',
    'Beach volleyball',
    'Dodgeball',
    'Baseball',
    'Cricket',
    'Snooker',
    'Handball',
]


def post_tweet(event, context):
    client = get_twitter_client_from_environment()
    message = get_tweet_message(ANIMALS, SPORTS)

    print(f"Posting: '{message}' to twitter")
    client.update_status(message)

    return {'message': message}


def get_tweet_message(animals: List[str], sports: List[str]) -> str:
    animal = random.choice(animals)
    sport = random.choice(sports)
    indefinite_article = get_indefinite_article(animal)
    return f"Ain't no rule that says {indefinite_article} {animal} can't play {sport}"


def get_indefinite_article(noun: str) -> str:
    """
    >>> get_indefinite_article('Elephant')
    'an'
    >>> get_indefinite_article('lion')
    'a'
    >>> get_indefinite_article('  ant')
    'an'
    >>> get_indefinite_article('hotel')
    'an'
    """
    normalised_noun = noun.lower().strip()

    if not normalised_noun:
        return 'a'

    if normalised_noun[0] in 'aeiou':
        return 'an'
    elif normalised_noun[0] == 'h':
        return get_indefinite_article(normalised_noun[1:])
    else:
        return 'a'


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
