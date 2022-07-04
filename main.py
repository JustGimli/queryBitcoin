from requests import Request,Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



def give_usd_bitcoin():
    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'5eab8521-9506-4ee0-8e37-de0ccc412d78',
        'Accept-Encoding': 'deflate, gzip',
        
    }

    bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


    try:
        
        
        session = Session()
        session.headers.update(headers)
        responce = session.get(bitcoin_api_url)
        json_file = json.loads(responce.text)
        price = round(json_file['data'][0]['quote']['USD']['price'], 2)  #сори, учу  js поэтому такое непотребство
        print(price)
        return price

    except (ConnectionError,Timeout,TooManyRedirects) as e:

        print(e)

