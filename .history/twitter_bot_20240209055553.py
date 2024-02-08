import tweepy 
import os
from dotenv import load_dotenv

#.envファイルを読み込む
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('consumer_secret')
bearer_token = os.getenv('bearer_token')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

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

tweet('これはテストです')