import tweepy 
import os
from dotenv import load_dotenv 
import time
from openai import OpenAI
import json

#特定の.envを読み込むため、path指定しロードさせる
dotenv_path = 'user_data.env'
load_dotenv(dotenv_path)


#openaiのAPIキーの設定
client = OpenAI(
    api_key=os.environ.get('API_KEY')
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
other_texts = []

def tweet_text(before_texts):
    # other_texts = []
    
    #テキスト生成のリクエストを送信
    for before_text in before_texts:
        if before_text:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "user", "content": f"何か豆知識を書いてください。但し{before_text}意外でお願いします。また、130文字以内でお願いします。"}
                ]
            )
            
            other_text = response.choices[0].message.content
            if other_text not in create_text_list and other_text not in other_texts:
                other_texts.append(other_text)
    
    # for other_text in other_texts:
    #     if other_text not in create_text_list and other_text not in message_list:
    #         message_list.append(other_text)
            


tweets_file = open('tweets.txt', 'r', encoding='utf-8')

tweet = json.load(tweets_file)

for file in tweet:
    text = file['tweet']['full_text']
    if '@' not in text:
        create_text_list.append(text)

print(f'create_text_list:{create_text_list}')
i = 0

while i<3: #ツイートの数が増えるなら i<1でいい。
    tweet_text(create_text_list)
    i+=1


def tweet(message):
    try:
        twitter.create_tweet(text=message)
        print('ツイートを投稿しました',message)
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)

for i in range(3): 
    if i < len(other_texts):  
        delete_n = [x.strip('\n') for x in other_texts] 
        tweet(delete_n[i]) 
        time.sleep(10)