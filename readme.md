# Telegram Bot Lambda Boilerplate using Zappa + Hug + Telepot

### Git Clone this repo

### Initial setup

```bash
pipenv --three
pipenv install
```

### Make sure you have installed Zappa and awscli in your project directory
```bash
pipenv install awscli
pipenv install zappa
```

create user with broad permissions (but not too broad)
run awscli and configure your api key

### Setup Your Project Variables

Open zappa_settings.json and adjust your configs

### create a AWS IAM role for zappa
(please refer to reference)

### Setup Your Telegram Bot's Key

If you dont have one please go to @botfather to get one

create a .env file with BOT_TOKEN='<yourkey>' with your key from botfather


### Deploy on AWS Lambda

Assuming you have sufficient permissions run the following commands in the shell

```bash
pipenv shell
zappa deploy
```

Take note of the endpoint of your bot. Will look similar to the following
add to .env file

```bash
WEBHOOK=https://xxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev
```
(works for ngrok also, just set it's url instead)

### Telling Telegram your Bot is alive

Send the following curl to Telegram to inform them of your endpoint. Replace the variables below with your own

run set_webhook.py

The reply returned should be True.

Speak to your bot!


### Updating your bot

Updates to your bot can be done and then sent to production using

```bash
zappa update
```

### Tips
1. ngrok (https://ngrok.com/) is a very good way to test your code before deploying to AWS lambda. Please refer to item 1 of the reference for details.

### Some useful reference
1.  https://medium.freecodecamp.org/how-to-build-a-server-less-telegram-bot-227f842f4706
2.  https://taiosolve.xyz/first-steps-with-aws-lambda-zappa-flask-and-python-3/
3. https://www.viget.com/articles/building-a-simple-api-with-amazon-lambda-and-zappa/
4.
https://github.com/kianhean/telegrambotawslambda