import time

import tweepy

# Credenciales de acceso
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Autenticarse con Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crear el objeto API
api = tweepy.API(auth)

# Tu tweet a ser publicado
tweet = 'Tweet programado para publicar automáticamente'

# Programar la publicación
while True:
    if time.strftime("%H:%M:%S") == '12:00:00':  # Programar la publicación a las 12:00
        api.update_status(tweet)
        print('Tweet publicado')
    time.sleep(1)
