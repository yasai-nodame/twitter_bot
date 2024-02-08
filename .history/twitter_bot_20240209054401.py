import tweepy 
import os
from dotenv import load_dotenv

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
bearer_token = os.environ['bearer_token']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

twitter = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    bearer_token=bearer_token,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def tweet(message):
    try:
        twitter.create_tweet(text=message)
        print('ツイートを投稿しました',message)
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)
        
tweet('これはテストです。')