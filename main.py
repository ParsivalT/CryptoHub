from cryptohub.hub import Coin
from time import sleep


BASE_URL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=COIN&tsyms=FORMAT'

def menu() -> tuple:
    print('=='*40)
    print(f'{"Wellcome to CryptoHub":^80}')
    print('=='*40)

    print('Enter the currency you want to monitor and the formatting type example: BTC, BRL')
    print('=='*40)

    """Validation Inputs"""
    coin = input('Enter the asset you want to monitor(BTC: bitcoin): ').upper()
    while (len(coin) < 3) or (len(coin) > 5) or (coin.isdigit()):
        print('Enter a valid value')
        coin = input('Enter the asset you want to monitor(BTC: bitcoin): ').upper()

    format = input('enter the format(BRL: brazilian coin): ').upper()
    while (len(format) < 3) or (len(format) > 5) or (format.isdigit()):
        print('Enter a valid value')
        format = input('enter the format(BRL: brazilian coin): ').upper()

    return coin, format


API = Coin(base_url=BASE_URL)
coin, format = menu()

current_value, time = API.check_price(coin, format)
print(current_value, time)