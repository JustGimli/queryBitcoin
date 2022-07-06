from aiogram import *
import configparser
from main.main import *
from main.send_email import *

config = configparser.ConfigParser()
config.read('config.ini')
token = config['bot']['token']

client = Bot(token)
dispatch = Dispatcher(client)


@dispatch.message_handler(commands=['btc'])
async def start_bot(message):
    print(message.chat.id)
    price_usd = give_usd_bitcoin()
    await client.send_message(message.chat.id,f'Цена биткоина: {price_usd}$')




try:
    executor.start_polling(dispatch)

except Exception as e:  

    send_email(e,'from bot-client')

    with open('bags.txt','w') as f:
        f.write(f'Ошибка в боте: {e}')


