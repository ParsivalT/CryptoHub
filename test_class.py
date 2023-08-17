import pytest
from cryptohub.hub import Coin
from main import menu

BASE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=COIN&tsyms=FORMAT'
COIN = Coin(base_url=BASE_URL)

def test_api():
    assert COIN.ping() == True

# TODO: create validation test

def test_validation():
    pass
    


