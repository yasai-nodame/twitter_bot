import tweepy

api_key = 'cawwZO'
token = 'AAAAAAAAAAAAAAAAAAAAAJwhsQEAAAAAildbhfcWpYCFjLgpKyXxYtHLe8I%3DEsF15VWceRCYOnIJrdOYabOYMnhTyFhrYFznhxf7QEyqC9fcud'
access_token = '1660501566082940928-KYOuBLg6tgFQUhmbxsU9Qv6YjlUUcf'
access_token_secret = 'Fe8YlviLv9HFoIMbr5IZALkcirEo3OfNBQipPOFYuR8aV'


auth = tweepy.OAuth1UserHandler(
    token,access_token,access_token_secret
)

api = tweepy.API(auth) #アカウント認証


# cawwZO