import tweepy

consumer_key  = 'cawwZO'
consumer_secret = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAildbhfcWpYCFjLgpKyXxYtHLe8I%3DEsF15VWceRCYOnIJrdOYabOYMnhTyFhrYFznhxf7QEyqC9fcud'
access_token = '1660501566082940928-KYOuBLg6tgFQUhmbxsU9Qv6YjlUUcf'
access_token_secret = 'Fe8YlviLv9HFoIMbr5IZALkcirEo3OfNBQipPOFYuR8aV'


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, 
    access_token, access_token_secret
)

api = tweepy.API(auth) #アカウント認証

tweet_text = 'これはテストです'

api.update_status(status=tweet_text)

print(api)
# cawwZO