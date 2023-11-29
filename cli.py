# Adicionando a possibilidade de usar como um CLI

import sys
from cryptohub.hub import Coin

BASE_URL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=COIN&tsyms=FORMAT'
API = Coin(BASE_URL)


current_value, time = API.check_price("BTC", "BRL")
print("=================================================")
print(f'BitCoin: R$ {current_value} Data:{time}')
print("=================================================")
