import pytest
from cryptohub.hub import Coin
from main import menu

BASE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=COIN&tsyms=FORMAT'

def test_api():
    coin = Coin(base_url=BASE_URL)
    value, time = coin.check_price('BTC', 'BRL')

    assert coin.ping() == True
    assert value.isdigit() == True

