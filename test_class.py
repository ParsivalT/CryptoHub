import pytest
from cryptohub.hub import Coin

BASE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=COIN&tsyms=FORMAT'

def test_api():
    coin = Coin(base_url=BASE_URL)

    assert coin.ping() == True



if __name__ == '__main__':
    test_api()
