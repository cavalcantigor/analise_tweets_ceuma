from tweepy import (
    API, Stream, OAuthHandler
)
from tt_keys import consumer_secret, consumer_key, access_token_secret, access_token
from ceuma_stream import StreamListenerCeuma


def timeline():
    # get tweets from timeline
    timeline_result = api.home_timeline()
    return timeline_result


def search_tweets(query):
    # get tweets that matches the query search
    search_result = api.search(query, text_mode='extended')
    return search_result


def print_tweets(tweets):
    # print tweets
    for tweet in tweets:
        print(tweet.text)


# set consumer key and consumer secret key
auth = OAuthHandler(consumer_key, consumer_secret)

# set access token and access token secret
auth.set_access_token(access_token, access_token_secret)

# create api object
api = API(auth)

listener = StreamListenerCeuma()
stream = Stream(auth, listener)
stream.filter(track=['ceuma', 'dino', 'gol'])
