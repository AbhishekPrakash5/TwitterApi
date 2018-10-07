# themodelbot

import tweepy as tp
import time
import os
import twitter_credentials


# login to twitter account api

auth = tp.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)
api = tp.API(auth)

os.chdir('EmmaWatson')

# iterates over pictures in EmmaWatson folder

for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(5)


