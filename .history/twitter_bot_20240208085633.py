import tweepy

api_key = 'vOgzOlmo3BXINpm59o0BVokS9'
api_key_secret = 'V3XjgAerGJBKLCJxhO5L5n3LC0sMbib2ygpd8ctBrAIfAHgkA1'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAildbhfcWpYCFjLgpKyXxYtHLe8I%3DEsF15VWceRCYOnIJrdOYabOYMnhTyFhrYFznhxf7QEyqC9fcud'

auth = tweepy.OAuth2BearerHandler(bearer_token)

client = tweepy.Client(auth) #アカウント認証

tweet_text = 'これはテストです'

# try:
#     api.update_status(status=tweet_text)
#     print('ツイートが投稿されました')
# except tweepy.TweepyException as e:
#     print('ツイートの投稿に失敗しました')

a = client.create_tweet(text=tweet_text)

print(a)

28385692