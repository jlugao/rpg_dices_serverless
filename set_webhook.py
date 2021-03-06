#!/usr/bin/python
from decouple import config

bot_token = config('BOT_TOKEN')

import telepot
bot = telepot.Bot(bot_token)

#Set AWS endpoint gateway
webhook = config('WEBHOOK')
result = bot.setWebhook(webhook)

if result:
    print(f'Webhook set to:{webhook}')

#terminate webhook if sth gets wrong
# bot.setWebhook("https://14c9bd96.ngrok.io")

print(bot.getMe())