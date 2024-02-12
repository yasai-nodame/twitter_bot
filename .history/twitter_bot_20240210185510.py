import tweepy 
import os
from dotenv import load_dotenv 
import schedule 
import time

#特定の.envを読み込むため、path指定しロードさせる
dotenv_path = 'user_data.env'
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
def tweet(message):
    try:
        twitter.create_tweet(text=message)
        print('ツイートを投稿しました',message)
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)

message_list = {
    'これはありです',
    'これはなしです',
    '私はYESです',
    'あああああああああ',
    'いいいいいいいいいいいい'
}

#test_bot.pyのコードを用いればreturn other_textで重複してないテキストを使えるためfor文である必要はない
#最初は20秒ごとに実行していき大丈夫であれば、24時間毎にしようかなと思う。
for message in message_list:
    schedule.every(20).seconds.do(tweet, message=message)
    
while True:
    schedule.run_pending()
    time.sleep(1)