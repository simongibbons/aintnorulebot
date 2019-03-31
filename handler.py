import os
import random
from typing import List

import tweepy

ANIMALS = [
    'dog',
    'cat',
    'raccoon',
    'manatee',
    'shark',
    'tiger',
    'hawk',
    'rattlesnake',
    'moose',
    'mongoose',
    'lion',
    'giraffe',
    'panda',
    'capybara',
    'dolphin',
    'porpoise',
    'tortoise',
    'turtle',
    'snapping turtle',
    'alligator',
    'crocodile',
    'rabbit',
    'shrew',
    'vole',
    'mole',
    'star-nosed mole',
    'naked mole rat',
    'rat',
    'sea urchin',
    'hedgehog',
    'boa constrictor',
    'snake',
    'python',
    'cobra',
    'blue tit',
    'great tit',
    'robin',
    'turkey',
    'chicken',
    'duck',
    'elk',
    'caribou',
    'goat',
    'sheep',
    'warthog',
    'pig',
    'meerkat',
    'cardinal bird',
    "Thompson's gazelle",
    'gazelle',
    'antelope',
    'dik-dik',
    'lamb',
    'goshawk',
    'hobby hawk',
    'eagle',
    'beaver',
    'otter',
    'cougar',
    'puma',
    'lynx',
    'leopard',
    'dingo',
    'barn owl',
    'tawny owl',
    'owl',
    'screech owl',
    'little owl',
    'penguin',
    'adelie penguin',
    'emperor penguin',
    'rock hopper penguin',
    'king penguin',
    'pelican',
    'flamingo',
    'aye-aye',
    'cormorant',
    'whale',
    'killer whale',
    'whale shark',
    'orca',
    'humpback whale',
    'sperm whale',
    'right whale',
    'hammerhead shark',
    'great white shark',
    'shag',
    'great bustard',
    'vulture',
    'turkey vulture',
    'greeb',
    'coley',
    'haddock',
    'pangasius',
    'small-mouth bass',
    'catfish',
    'gorilla',
    'western lowland gorilla',
    'chimpanzee',
    'mandrill',
    'baboon',
    'gibbon',
    'siamang gibbon',
    'bream',
    'orangutan',
    'frog',
    'toad',
    'hare',
    'leveret',
    'goose',
    'buzzard',
    'gyrfalcon',
    'worm',
    'beetle',
    'scarab beetle',
    'spider',
    'black widow spider',
    'tarantula',
    'daddy long-legs',
    'fly',
    'mosquito',
    'tsetse fly',
    'flea',
    'tick',
    'deer tick',
    'tapeworm',
    'eel',
    'electric eel',
    'cheese mite',
    'newt',
]

SPORTS = [
    'basketball',
    'football',
    'tennis',
    'rugby',
    'water polo',
    'lacrosse',
    'curling',
    'golf',
    'ultimate frisbee',
    'beach volleyball',
    'dodgeball',
    'baseball',
    'cricket',
    'snooker',
    'handball',
    'Eton fives',
    'kabadi',
    'hurling',
    'chess',
    'Aussie rules football',
    'go',
    'checkers',
    'chinese checkers',
    'draughts',
    'backgammon',
    'bridge',
    'whist',
    'darts',
    'Monopoly',
    'pool',
    'bar billiards',
    'lawn tennis',
    'real tennis',
    'table tennis',
    'ping-pong',
    'rounders',
    'polo',
    'frisbee golf',
    'fives',
    'kwik cricket',
    'croquet',
    'crown green bowls',
    'petonque',
    'bowls',
    'ten-pin bowling',
    'whack-a-mole',
    'volleyball',
    'netball',
    'badminton',
    'squash',
    'racquetball',
    'swingball',
    'tee-ball',
    'clock golf',
    'clock darts',
    'billiards',
    'poker',
    'faro',
    "Texas hold 'em",
    'five card stud'
    'Omaha hi-lo',
    'blackjack',
    'pick-up stix',
    'pelota',
    'jai alai',
    'rock paper scissors',
    'tiddlywinks',
    'touch rugby',
    'American football',
    'soccer',
    'touch football',
    'rugby league',
    'rugby union',
    'major league baseball',
    'korfball',
    'softball',
    'quidditch',
    'foosball',
    'table football',
    'bagatelle',
    "shove ha'penny",
    'cribbage',
    'gaelic football',
    'Winchester College football',
    'goalball',
    'hockey',
    'ice hockey',
    'field hockey',
    'shinty',
    'elephant polo',
    'segway polo',
    'tag',
    'it',
    'british bulldogs',
    'hide and seek',
    'hopscotch',
    'paintball',
    'e-sports',
    'beer pong',
    'air hockey',
    'subbuteo',
    'bocce',
    'boules',
    'shuffleboard',
    'skittles',
    'skee ball',
    'the mesoamerican ball game',
    'calvinball',
]


def post_tweet(event, context):
    client = get_twitter_client_from_environment()
    print(f"Have {len(ANIMALS)} animals")
    print(f"Have {len(SPORTS)} sports")

    message = get_tweet_message(ANIMALS, SPORTS)

    print(f"Posting: '{message}' to twitter")
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
