import tweepy

consumer_key = 'vOgzOlmo3BXINpm59o0BVokS9'
consumer_key_secret = 'V3XjgAerGJBKLCJxhO5L5n3LC0sMbib2ygpd8ctBrAIfAHgkA1'
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAyNKYY9uSNAord17oljMCo%2B6nchQ%3D9QxO9TTZgTyMmImzTXrGYxS6KWEV7IOOWIYBQYPDaZgXiUAWTR'
access_token = '1660501566082940928-EmA2Zw6Xl0cakejPEDr0fBsPYFHTnX'
access_token_secret = 'DUlu2nkwmekekHL0hkMHKFHL6vIOPeC14q3VB6uvkoLe2'

twitter = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_key,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# api = tweepy.Client(auth) #アカウント認証

tweet_text = 'これはテストです'

# try:
#     api.update_status(status=tweet_text)
#     print('ツイートが投稿されました')
# except tweepy.TweepyException as e:
#     print('ツイートの投稿に失敗しました')

try:
    twitter.create_tweet(text=tweet_text)
    print('ツイートが投稿されました')
except tweepy.TweepyException as e:
    print('ツイートの投稿に失敗しました',e)