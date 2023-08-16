import requests
import logging

BASE_URL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=COIN&tsyms=FORMAT'

LOG_FORMAT = 'Data/Hora: %(asctime)s | LEVEL:%(levelname)s | Mensagem:%(message)s'
logging.basicConfig(filename="relatorio.log", level=logging.ERROR, format=LOG_FORMAT)
LOG = logging.getLogger()

class Coin:
    def __init__(self, base_url: str):
        self.base_url = base_url
        

    def ping(self) -> bool:
        if requests.get(self.base_url).status_code == 200:
            return True

        else: 
            logging.WARNING('Api Offline, please wait one moment')
            return False


    def check_price(self, coin_id: str, format: str) -> tuple:

        api = self.base_url.replace('COIN', coin_id)
        api = api.replace('FORMAT', format)
        data_base = requests.get(api).json()
        data_base = data_base['RAW'][coin_id]
        price = data_base[format]['PRICE']
        time = data_base[format]['LASTUPDATE']

        

        return price,time


coin = Coin(BASE_URL)

print(coin.check_price('BTC', 'BRL'))
