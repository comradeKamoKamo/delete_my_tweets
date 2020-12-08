#!/usr/bin/env python

"""
ツイートをすべて自動削除する
"""

import os
import time

import tweepy
from tweepy.error import TweepError

USERNAME = "kam0_2"

def get_api():
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def main():
    # OAuth
    api = get_api()
    try:
        get_tweets_and_del(api)
    except TweepError:
        time.sleep(15)
        main()

def get_tweets_and_del(api):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = USERNAME, include_rts = True).items():
        api.destroy_status(tweet.id)

if __name__ == "__main__":
    main()
