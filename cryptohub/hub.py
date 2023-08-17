import requests
import logging
from datetime import datetime

# Base URL for the cryptocurrency price API
"""BASE_URL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=COIN&tsyms=FORMAT' """

# Log record format
LOG_FORMAT = 'Date/Time: %(asctime)s | LEVEL:%(levelname)s | Message:%(message)s'

# Configure the logging module
logging.basicConfig(filename="relatorio.log", level=logging.DEBUG, format=LOG_FORMAT)
LOG = logging.getLogger()

class Coin:
    def __init__(self, base_url: str):
        self.api = base_url
        self.default_url =  'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD'
        
    # Check if the API is online
    def ping(self) -> bool:
        if requests.get(self.default_url).status_code == 200:
            return True
        else:
            # Log a warning if the API is offline
            logging.error('API Offline, please wait a moment')


    # Get the price and last update time of a cryptocurrency
    def check_price(self, coin_id: str, format: str) -> tuple:

        try:
            if self.ping():

                # Replace placeholders in the URL to get the full API URL
                api = self.api.replace('COIN', coin_id)
                api = api.replace('FORMAT', format)
                
                # Make a GET request to the API and retrieve the JSON response
                data_base = requests.get(api).json()
                
                # Extract relevant data from the JSON
                data_base = data_base['RAW'][coin_id]
                price = data_base[format]['PRICE']
                time = data_base[format]['LASTUPDATE']
                
                # Format the price and time
                price = "{:,.2f}".format(price)
                time = datetime.fromtimestamp(time).strftime('%x %X')
                
                # Return a tuple with the formatted price and time
                return price, time
            
            else:
                raise ConnectionError("API OFFILINE")
            
        except:
            print('offline API please try again later')
            LOG.warning('Offline API during program execution')

