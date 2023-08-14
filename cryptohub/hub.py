import requests
import logging

BASE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BRL'

LOG_FORMAT = 'Data/Hora: %(asctime)s | LEVEL:%(levelname)s | Mensagem:%(message)s'
logging.basicConfig(filename="relatorio.log", level=logging.ERROR, format=LOG_FORMAT)
LOG = logging.getLogger()

class Coin:
    def __init__(self, base_url: str):
        self.base_url = base_url
        

    def ping(self) -> bool:
        return requests.get(self.base_url).status_code


