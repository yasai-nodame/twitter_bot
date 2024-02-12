import tweepy 
import os
from dotenv import load_dotenv 
import schedule 
import time

#特定の.envを読み込むため、path指定しロードさせる
dotenv_path = 'test_data.env'
load_dotenv(dotenv_path)


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
def tweet():
    try:
        twitter.create_tweet(text='これはテストです')
        print('ツイートを投稿しました')
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)

tweet()

# schedule.every(20).seconds.do(tweet)

# while True:
#     #スケジュールされたジョブの実行
#     schedule.run_pending()
#     time.sleep(1)