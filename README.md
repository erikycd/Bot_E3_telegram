# Bot_E3_telegram

## Bot designed with APIs of both [Telegram](https://github.com/python-telegram-bot/python-telegram-bot) and [Wolframalpha](https://products.wolframalpha.com/api/documentation/). 

## Bot currently available in telegram and mounted in an instance of [AWS-EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc)

### Installation requirements

You should install or upgrade python-telegram-bot by the command:

```
$ pip install python-telegram-bot --upgrade
```

It would be needed the wolframalpha libraries. Install them with:
```
$ pip install wolframalpha
```

### Main execution

A diagram of basic implementation is shown below:

<p align="center">
  <img width="60%" src="https://raw.githubusercontent.com/erikycd/Bot_E3_telegram/main/Diagram_1.png">
</p>

After creating a bot in telegram with the help of [@BotFather](https://core.telegram.org/bots#6-botfather). Insert your token in the line:
```python
updater =  Updater('', use_context=True) # Insert here API code of telegram
```
Moreover, you must insert your token of wolframalpha in line:
```python
app_id = '' # Insert here API code of wolframalpha 
client = wolframalpha.Client(app_id)
```

<p align="center">
  <img width="40%" src="https://github.com/erikycd/Bot_E3_telegram/blob/main/ezgif.com-video-to-gif.gif">
</p>

### Visit him at: https://t.me/E3_demoBot
