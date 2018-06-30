import hug
import telepot
from telepot.exception import TelegramError
import json
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from dices import lanca_d4, lanca_d6, lanca_d8, lanca_d10, lanca_d12, lanca_d20
from decouple import config

bot_token = config('BOT_TOKEN')
bot = telepot.Bot(bot_token)


# @hug.post('/start')
# def receive(body):
#     """ Simple Hug Server """
#     print(body)
#     msg = json.loads(body)['message']
#     content_type, chat_type, chat_id = telepot.glance(message)
#     bot.sendMessage(chat_id, 'Bem vindo ao bot de rolar dados do Tincani')
#     return output

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
    # print(body)
    output = read_message(body)
    # print(output)
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
    print(chat_id)
    if content_type == 'text' and message['text'][0] == '/':
        if message['text'][:2] == '/d':
            valor = dices[message['text'][1:]]()
            bot.sendMessage(chat_id, f'{valor}')
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
    # print(message)
    valor = dices[query_data]()
    print(chat_id)
    
    bot.sendMessage(chat_id, text=f'{valor}')

    return True