# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:06:13 2021

@author: Erik

API Bot to reply Telegram messages with Wolframalpha

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import wolframalpha
import pandas as pd

#%%

def start(update, context):
    
    # Save user info in dataframe
    user_name = update.message.from_user['first_name']
    user_lastname = update.message.from_user['last_name']
    user_username = update.message.from_user['username']
    user_id = update.message.from_user['id']
    user_info = [user_name, user_lastname, user_username, user_id]

    Info = pd.DataFrame(user_info , index = ['User Name','User Lastname','Username','User ID'])
    Info = Info.transpose()
    
    data = pd.read_excel('Info.xlsx' , engine='openpyxl')
    
    frames = [data, Info]
    data = pd.concat(frames)

    data.to_excel('Info.xlsx', index = False, header = True)
    print(data)
    
    update.message.reply_text('Hello {}, I am E3 demo bot' .format(update.message.from_user['first_name']))
    
def query(res):
    if res['@success'] == 'false':
        none = 'Question cannot be resolved, it might be mistyped.'
        return none
    else:
        # pod is the whole answers
        pod = res['pod']
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
    
        if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
            result = pod1['subpod']['plaintext']
            return result
        else:
            # find the wiki answer
            for sub in pod:
                subpod = sub['@title']
                if subpod == 'Wikipedia summary':
                    result_wiki = sub['subpod']['plaintext']
                    result_link = sub['subpod']['infos']['info']['link']['@url']
                    return result_wiki
    
def reply(update, context):
    app_id = '' # Insert here API code of wolframalpha 
    client = wolframalpha.Client(app_id)
    user_query = update.message.text
    
    res = client.query(user_query)
    specific_res = query(res)
    
    update.message.reply_text(specific_res)
    
def main():
    
    updater =  Updater('', use_context=True) # Insert here API code of telegram
    
    updater.dispatcher.add_handler(CommandHandler('start' , start))
    
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
    
    # Start
    updater.start_polling()
    print("I am alive now")
    
    # Stay waiting
    updater.idle()
    
    
if __name__ == "__main__":
    main()

