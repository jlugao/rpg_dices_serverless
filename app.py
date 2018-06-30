import hug
import telepot
from telepot.exception import TelegramError
import json
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from dices import lanca_d4, lanca_d6, lanca_d8, lanca_d10, lanca_d12, lanca_d20
from decouple import config
import re

bot_token = config('BOT_TOKEN')
bot = telepot.Bot(bot_token)

dices = {
        'd4': lanca_d4,
        'd6': lanca_d6,
        'd8': lanca_d8,
        'd10': lanca_d10,
        'd12': lanca_d12,
        'd20': lanca_d20
    }

@hug.post('/')
def receive(body):
    """ Simple Hug Server """
    output = read_message(body)
    return output


def read_message(message):
    """ Returns Message as Dictionary """

    if not isinstance(message, dict):
        msg = json.loads(message)['message']
    else:
        msg = message
 
    if 'callback_query' in msg:
        on_callback_query(msg['callback_query'])
    elif 'message' in msg:
        on_chat_message(msg['message'])
        
    return 'OK'


def on_chat_message(message):
    """ Handle JSON Message from Telegram
        message - string
        http://telepot.readthedocs.io/en/latest/reference.html
    """
    content_type, chat_type, chat_id = telepot.glance(message)
    try:
        user = message['from']['username']
    except:
        try:
            user = message['from']['last_name']
        except:
            try:
                user = message['from']['first_name']
            except:
                user = message['from']['id']


    msg = message['text']
    print(user)
    print(message)
    try:
        pass
    except:
        return
    if content_type == 'text' and msg[0] == '/':
        if msg[:2] == '/d':
            try:
                valor = dices[message['text'][1:]]()
                bot.sendMessage(chat_id, f'{user} - {valor}')
            except:
                bot.sendMessage(chat_id, f'dado {msg} não encontrado')
        elif re.match('\/\dd\d+',msg):
            valor = ', '.join([ str(dices[msg[2:]]()) for i in range(int(msg[1]))])
            bot.sendMessage(chat_id, f'{user} - {valor}')
        else:
            bot.sendMessage( chat_id,
                text = 'Escolha um dado',
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                        InlineKeyboardButton(text='d4', callback_data='d4'),
                        InlineKeyboardButton(text='d6', callback_data='d6'),
                        ],
                        [
                        InlineKeyboardButton(text='d8', callback_data='d8'),
                        InlineKeyboardButton(text='d10', callback_data='d10'),
                        ],
                        [
                        InlineKeyboardButton(text='d12', callback_data='d12'),
                        InlineKeyboardButton(text='d20', callback_data='d20')
                        ]
                    ]
                )
            )
 
def on_callback_query(message):
    """
        do sth similar to on_chat_message
    """
    query_id, from_id, query_data  = telepot.glance(message, flavor='callback_query')
    chat_id = message['message']['chat']['id']
    valor = dices[query_data]()
    try:
        user = message['from']['username']
        text = message['data']
        
        bot.sendMessage(chat_id, text=f'{user} - {text}\n{valor}')
    except:
        pass


    return True
