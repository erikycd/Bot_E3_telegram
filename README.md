# Bot_E3_telegram

The designed chatbot follows the guides for connecting the APIs of [Telegram](https://github.com/python-telegram-bot/python-telegram-bot), [Wolframalpha](https://products.wolframalpha.com/api/documentation/) and [Twitter](https://realpython.com/twitter-bot-python-tweepy/). 

1. The idea behind this project is to show the conversational skills of the Wolframalpha artificial intelligence by means of Telegram. It can be also used as a bot for data inquiries to search in both Wolframalpha and Wikipedia datasets. 
2. This bot is also designed for estimating the real risk transmitted by a Twitter post.

This bot is currently available in telegram and mounted on [AWS-EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc) free instance.

### - Main diagram

A diagram of the implementation is shown below:

<p align="center">
  <img width="60%" src="https://raw.githubusercontent.com/erikycd/Bot_E3_telegram/main/Diagram_2.png">
</p>

### - Installation requirements

Install or upgrade python-telegram-bot by the command:

```
$ pip install python-telegram-bot --upgrade
```

Wolframalpha libraries are required. Install them with:
```
$ pip install wolframalpha
```

Install twitter libraries by:
```
$ pip install tweepy
```

### - Basic configuration

After creating a bot in telegram with the help of [@BotFather](https://core.telegram.org/bots#6-botfather). Insert your token in the line:
```python
updater =  Updater('', use_context=True) # Insert here API code of telegram
```
Moreover, you should be registered as [Wolframalpha developer](https://products.wolframalpha.com/simple-api/documentation/), then insert your token in line:
```python
app_id = '' # Insert here API code of wolframalpha 
client = wolframalpha.Client(app_id)
```

### - Conversational results

<p align="center">
  <img width="40%" src="https://github.com/erikycd/Bot_E3_telegram/blob/main/ezgif.com-video-to-gif.gif">
</p>

### - Visit him at: https://t.me/E3_demoBot
