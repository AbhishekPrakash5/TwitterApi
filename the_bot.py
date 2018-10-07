# themodelbot

import tweepy as tp #python library for accessing twitter via api
import time
import os
import twitter_credentials


# login to twitter account api

#setting the consumer_key,consumer_secret,access_token,access_secret to a single variable auth
auth = tp.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) #OAuthHandler helps to authenticate with the twitter server in order to login
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_secret)  #setting the access toke, using function within the tp lib
api = tp.API(auth) #creating the api var and login via tp.API() function


# iterates over pictures in EmmaWatson folder

os.chdir('EmmaWatson') #move in to the image folder

#looping over each file
for model_image in os.listdir('.'): #listdir('.'){it is in os} = lists all the file in the folder 
    api.update_with_media(model_image) #tp fuction to post photo
    time.sleep(5) #set time interval to pause before posting another pic


