import tweepy 
import os




env = os.environ
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

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

print(env)