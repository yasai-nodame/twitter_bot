import tweepy

consumer_key  = 'cawwZO'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAildbhfcWpYCFjLgpKyXxYtHLe8I%3DEsF15VWceRCYOnIJrdOYabOYMnhTyFhrYFznhxf7QEyqC9fcud'
access_token = '1660501566082940928-KYOuBLg6tgFQUhmbxsU9Qv6YjlUUcf'
access_token_secret = 'Fe8YlviLv9HFoIMbr5IZALkcirEo3OfNBQipPOFYuR8aV'


auth = tweepy.OAuth2BearerHandler(bearer_token)

client = tweepy.Client(auth) #アカウント認証

tweet_text = 'これはテストです'

# try:
#     api.update_status(status=tweet_text)
#     print('ツイートが投稿されました')
# except tweepy.TweepyException as e:
#     print('ツイートの投稿に失敗しました')

print(client)