import tweepy 
import os
from dotenv import load_dotenv 
import schedule 
import time
from openai import OpenAI
import json

#特定の.envを読み込むため、path指定しロードさせる
dotenv_path = 'user_data.env'
load_dotenv(dotenv_path)


#openaiのAPIキーの設定
client = OpenAI(
    api_key='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'
)

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


create_text_list = [] #twitterで取得したツイート部分のテキストリスト
unique_list = []

def tweet_text(before_texts):
    other_texts = []
    
    #テキスト生成のリクエストを送信
    for before_text in before_texts:
        if before_text:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": "こんにちは"},
                    {"role": "user", "content": f"何か豆知識を書いてください。但し{before_text}意外でお願いします。また、130文字以内でお願いします。"}
                ]
            )
    
            #リクエストした回数分リストに追加
            other_texts.append(response.choices[0].message.content)
    
    for other_text in other_texts:
        if other_text not in create_text_list and other_text not in unique_list:
            unique_list.append(other_text)


tweets_file = open('tweets.txt', 'r', encoding='utf-8')

tweet = json.load(tweets_file)

for file in tweet:
    text = file['tweet']['full_text']
    if '@' not in text:
        create_text_list.append(text)

# print(create_text_list)
i = 0

while i<3:
    tweet_text(create_text_list)
    message_list = unique_list[i]
    i+=1


def tweet(message):
    try:
        twitter.create_tweet(text=message)
        print('ツイートを投稿しました',message)
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)


#test_bot.pyのコードを用いればreturn other_textで重複してないテキストを使えるためfor文である必要はない
#最初は20秒ごとに実行していき大丈夫であれば、12時間毎にしようかなと思う。
for message in message_list:
    tweet(message)
    time.sleep(10)