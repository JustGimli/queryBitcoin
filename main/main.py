from requests import Request,Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import configparser
from main.send_email import *



def give_usd_bitcoin():
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':conf['api']['api_key'],
        'Accept-Encoding': 'deflate, gzip',
        
    }

    bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


    try:
        
        session = Session()
        session.headers.update(headers)

        responce = session.get(bitcoin_api_url)
        json_file = json.loads(responce.text)

        return round(json_file['data'][0]['quote']['USD']['price'], 2)  #сори, учу  js поэтому такое непотребство

    except (ConnectionError,Timeout,TooManyRedirects) as e:
        send_email(e,'from api-currency')
        with open('bags.txt','w') as f:
            f.write(f'Ошибка в api:{e}')

