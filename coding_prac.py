# -*- coding: utf-8 -*-
import requests


class ApiError(Exception):
    pass


def get_stock_price(symbol):
    """Retrieve the latest stock information for the provided symbol.
    """
    api_key = 'CFHRL3LXYXSGU540'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    r = requests.get(url)
    r_json = r.json()
    if 'Error Message' in r_json:
        raise ApiError(r_json['Error Message'])
    data = r_json.get('Time Series (5min)', {})
    data = data[next(iter(data))]
    return {k.split(' ')[-1]: float(v) for k, v in data.items()}


class Cache(object):
    def __init__(self):
        self.stock_list = []

    def get_stock_price(self,symbol):
        self.stock_list.sort(key="Stock_name")
        low = ord("A")
        high = ord("Z")
        mid = (low+high)//2 
        while()
                sort_list


        for val in self.stock_list:
            if val["stock_name"]== symbol:
                return val
            else:
                data = get_stock_price(symbol)
                self.append_stock_list(data)

        

    
    def append_stock_list(self,data):
        return self.stock_list.append(data)


    def get(self, symbol):
        return get_stock_price(symbol)


cache = StockPriceCache()

cache.get('IBM')
cache.get('TWLO')