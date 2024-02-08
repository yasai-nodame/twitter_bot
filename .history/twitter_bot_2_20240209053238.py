import tweepy 

consumer_key = 'ChoInuRj2VhgqfzjTtFQyGMxL'
consumer_secret = 'CrRPltuL8FpDti7izMgXGn8Vwgh9QTEWf5S6WdIqbdEvfZrdsA'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAVOS0xtiAyq0B%2FJUC7YqKv2DBTxo%3D3f4trrmB5oG1aOiVtxOg8rhhelcMmiyKwmt2O0RdhmID85voFC'
access_token = '1660501566082940928-hOZPEKOKMZcy8pyFreEdeyLtAlbCrG'
access_token_secret = 't1HVIKR5wlf3LHTlgjC3VhUzsJPEp68UivsZb0Ev3St9G'

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