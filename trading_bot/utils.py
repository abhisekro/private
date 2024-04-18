import os
import ccxt
import pandas as pd
import numpy as np

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    return ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret
    })

def fetch_ohlcv(symbol, timeframe, limit):
    binance = get_binance_client()
    data = binance.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms') 
    return df
