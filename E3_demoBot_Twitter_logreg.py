# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:06:13 2021

@author: Erik
"""


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import wolframalpha
#import tkinter as Tk
#from tkinter import *
import pandas as pd

# Global for twitter
import validators
from tweet_processing_logreg import tweet_prediction


def start(update, context): # Saving user information in excel
    
    user_name = update.message.from_user['first_name']
    user_lastname = update.message.from_user['last_name']
    user_username = update.message.from_user['username']
    user_id = update.message.from_user['id']
    user_info = [user_name, user_lastname, user_username, user_id]

    Info = pd.DataFrame(user_info , index = ['User Name','User Lastname','Username','User ID'])
    Info = Info.transpose()
    
    #print('Info:',Info)
    
    data = pd.read_excel('Info.xlsx' , engine='openpyxl')
    #print('Data:',data)
    
    frames = [data, Info]
    data = pd.concat(frames)
    #data.append(Info, ignore_index = False)
    #print('Full:',data)

    data.to_excel('Info.xlsx', index = False, header = True)
    print(data)
    
    # Info_file = 'Users.csv'
    # with open(Info_file, mode='w') as f:
    #     Info_names.to_csv(f)
    
    update.message.reply_text('Hello {}, I am E3 demo bot' .format(update.message.from_user['first_name']))

def user_info(update, context): # For reading user info and displaying
    
    data = pd.read_excel('Info.xlsx' , engine='openpyxl')
    data_show = data.tail(5)
    print(data_show)
    update.message.reply_text(str(data_show))
    
def query_info(update, context): # For reading queries and displaying
    
    data = pd.read_excel('Query.xlsx' , engine='openpyxl')
    data_show = data.tail(5)
    print(data_show)
    update.message.reply_text(str(data_show))
    
def query(update, res):
    if res['@success'] == False:
        none = 'Question cannot be resolved, it might be mistyped.'
        #print('Question cannot be resolved')
        return none
    else:
        # pod is the whole answers
        pod = res['pod']
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
        #if (('definition' in pod1['@title'].lower()) or (pod1.get('@primary','false')) == 'true'):
        #if ('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()): 
        result = pod1['subpod']['plaintext']
        print(result)
        update.message.reply_text(result)
        #return result
        #else:
        # find the wiki answer
        for sub in pod:
            subpod = sub['@title']
            if subpod == 'Wikipedia summary':
                result_wiki = sub['subpod']['plaintext']
                result_link = sub['subpod']['infos']['info']['link']['@url']
                print(result_wiki)
                update.message.reply_text(result_wiki)
                #print('More information at:', result_link)
                #return result
                
def save_query(update, user_query): # Saving query in excel
    user_id = update.message.from_user['id']
    info_query = [user_id, user_query]
    Query = pd.DataFrame(info_query , index = ['User ID','Query'])
    Query = Query.transpose()
    data = pd.read_excel('Query.xlsx' , engine='openpyxl')
    frames = [data, Query]
    data = pd.concat(frames)
    data.to_excel('Query.xlsx', index = False, header = True)
    
    
def reply(update, context):
    app_id = 'W9QYJ6-8AARE5HVRL' 
    client = wolframalpha.Client(app_id)
    user_query = update.message.text
    save_query(update, user_query)
    
    valid = validators.url(user_query) # Checking whether is a valid link or not
    if valid==True:
        tweet_id = user_query.split('/')[-1]
        print("Url is valid from twitter with ID:", tweet_id)
        pred = tweet_prediction(update,tweet_id)
        update.message.reply_text('We estimate the current tweet is ' + str(round(pred, 2)) + '% a real emergency')
    else: # In case of normal text query
        res = client.query(user_query)
        query(update,res)
    
    #specific_res = next(res.results).text
    #update.message.reply_text(specific_res)
    
    
def main():
    
    updater =  Updater("1749106292:AAHtkm__rFYwYPhNJzCcvP5ytwUIDHlKYfw", use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start' , start))
    
    updater.dispatcher.add_handler(CommandHandler('user_info' , user_info))
    
    updater.dispatcher.add_handler(CommandHandler('query_info' , query_info))
    
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
    
    # Start
    updater.start_polling()
    print("I am alive now")
    
    # Stay waiting
    updater.idle()
    
    
if __name__ == "__main__":
    main()


