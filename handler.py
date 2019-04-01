import os
from pathlib import Path
import random
from typing import List

import tweepy


def post_tweet(event, context):
    animals = load_data_file('animals.txt')
    sports = load_data_file('sports.txt')

    print(f"Have {len(animals)} animals")
    print(f"Have {len(sports)} sports")

    message = get_tweet_message(animals=animals, sports=sports)

    print(f"Posting: '{message}' to twitter")
    client = get_twitter_client_from_environment()
    client.update_status(message)

    return {'message': message}


def get_tweet_message(animals: List[str], sports: List[str]) -> str:
    animal = random.choice(animals)
    sport = random.choice(sports)
    indefinite_article = get_indefinite_article(animal)
    return f"Ain't no rule says {indefinite_article} {animal} can't play {sport}"


def get_indefinite_article(noun: str) -> str:
    """
    >>> get_indefinite_article('Elephant')
    'an'
    >>> get_indefinite_article('lion')
    'a'
    >>> get_indefinite_article('  ant')
    'an'
    """
    normalised_noun = noun.lower().strip()

    if not normalised_noun:
        return 'a'

    if normalised_noun[0] in 'aeiou':
        return 'an'
    else:
        return 'a'


def load_data_file(file_name: str) -> List[str]:
    file_path = Path(__file__).parent / 'data' / file_name
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip() != '']


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
