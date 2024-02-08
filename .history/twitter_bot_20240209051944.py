import tweepy

consumer_key = 'nr6cosWErlrdf7HnQVGQmQllM'
consumer_secret = '0kMDA7SaUyh8dhWhkt6EL3M6hpMgqvT5LGFtaxjEms3ljLkG5R'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJchsQEAAAAAVxTz6oqpgqcCIAU0DBhQ3sUzxxE%3DEewDsrAFvBzd6bLlKHBZUyYHzAv0QgbQWl8Ak20wLknWLOjNx8'
access_token = '809600317406908416-56nZyY661zvRpcIzvr0wU0zUgdN7zxa'
access_token_secret = 'x2rfv2Zpg97Sp5kwMqFfsulHZxWI1jKdZ2gUzsju4mBJ2'

# #OAuth2.0の認証フローを開始
# auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

# #TweepyのAPIオブジェクトを作成
# api = tweepy.API(auth)

# #認証が成功したかを確認
# if not api:
#     print('認証失敗')
# else:
#     print('認証成功')
    

#TweepyでTwitter APIにアクセス
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)
client = tweepy.Client(auth)

def tweet(message):
    try:
        client.create_tweet(text=message)
        print('ツイートが投稿されました',message)
    except tweepy.TweepyException as e:
        print('ツイートの投稿に失敗しました',e)
#CLient_Secret 6N6Ork9Gshtt1lY-mGMqhjw8vUTBLqwkubtS_anQ3cbJzAvscc
# Client ID V0c4WmFMY2NGdkNyU3dDNTVFUjE6MTpjaQ
# API KEY nr6cosWErlrdf7HnQVGQmQllM
# API SECRET 0kMDA7SaUyh8dhWhkt6EL3M6hpMgqvT5LGFtaxjEms3ljLkG5R
# bearer_token  AAAAAAAAAAAAAAAAAAAAAJchsQEAAAAAVxTz6oqpgqcCIAU0DBhQ3sUzxxE%3DEewDsrAFvBzd6bLlKHBZUyYHzAv0QgbQWl8Ak20wLknWLOjNx8
# access token 809600317406908416-56nZyY661zvRpcIzvr0wU0zUgdN7zxa
# access token secret x2rfv2Zpg97Sp5kwMqFfsulHZxWI1jKdZ2gUzsju4mBJ2
