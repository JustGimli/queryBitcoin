from pydoc import cli
from aiogram import *
import configparser
from main import *

config = configparser.ConfigParser()
config.read('config.ini')
token = config['bot']['token']

client = Bot(token)
dispatch = Dispatcher(client)


@dispatch.message_handler(commands=['start'])
async def start_bot(message):
    price_usd = give_usd_bitcoin()
    await client.send_message(message.chat.id,f'Цена биткоина: {price_usd}$')







try:
    executor.start_polling(dispatch)

except Exception as e:  #сделать отправку багов на почту
    with open('bags.txt','w') as f:
        f.write(f'Ошибка {e}')


