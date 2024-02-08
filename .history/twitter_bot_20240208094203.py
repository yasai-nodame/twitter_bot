import tweepy

consumer_key = 'vOgzOlmo3BXINpm59o0BVokS9'
consumer_secret = 'V3XjgAerGJBKLCJxhO5L5n3LC0sMbib2ygpd8ctBrAIfAHgkA1'
access_token = '1660501566082940928-EmA2Zw6Xl0cakejPEDr0fBsPYFHTnX'
access_token_secret = 'DUlu2nkwmekekHL0hkMHKFHL6vIOPeC14q3VB6uvkoLe2'

auth = tweepy.OAuthHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet_text = 'これはテストです'

try:
    api.update_status(status=tweet_text)
    print('ツイートが投稿されました')
except tweepy.TweepyException as e:
    print('ツイートの投稿に失敗しました', e)