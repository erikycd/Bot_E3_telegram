# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:09:20 2021

@author: Erik
"""

# Importing for twitter:
import tweepy
import pandas as pd
from sklearn import preprocessing
import pickle


def tweet_prediction(update, tweet_id):
    # KEYS
    consumer_key = " "
    consumer_secret = " "
    access_token = " "
    access_token_secret = " "
      
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)
    # calling the api 
    api = tweepy.API(auth)
    # Retriving status
    status = api.get_status(tweet_id)
    # Retriving data
    message = status.text 
    user = status.user.screen_name
    location = status.user.location
    date = status.created_at
    update.message.reply_text('Twitter ID valid: ' + tweet_id)
    
    # Loading vectorizer
    filename_vectorizer = 'vectorizer.pkl'
    loaded_vectorizer = pickle.load(open(filename_vectorizer, 'rb'))

    # Loading model for new prediction
    filename_model = 'logreg_model.sav'
    loaded_model = pickle.load(open(filename_model, 'rb'))

    #% Inference on new data
    tweet_text = [message]
    tweet_vector = loaded_vectorizer.transform(tweet_text)
    tweet_array = tweet_vector.toarray()
    tweet_norm = preprocessing.normalize(tweet_array)
    
    prediction_2 = loaded_model.predict_proba(tweet_norm)
    proba = prediction_2[0,1]
    print(f'We estimate the current tweet is {proba:.2f}% a real emergency')
    
    # Saving info
    tweet_info = [user, message, location, date, proba]
    Info = pd.DataFrame(tweet_info , index = ['User Name','Message','Location','Posting date','Emergency prob'])
    Info = Info.transpose()    
    data = pd.read_excel('Info_tweets.xlsx' , engine='openpyxl')
    frames = [data, Info]
    data = pd.concat(frames)
    data.to_excel('Info_tweets.xlsx', index = False, header = True)
    
    return proba








