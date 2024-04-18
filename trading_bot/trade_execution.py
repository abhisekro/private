import ccxt  # Make sure you have CCXT installed: pip install ccxt

from config import api_key, api_secret  # Import your API keys from config.py

def execute_order(symbol, side, quantity, order_type='MARKET'):
    binance = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret
    })

    try:
        order = binance.create_order(symbol, type=order_type, side=side, amount=quantity)
        print(f"{side} order for {quantity} {symbol} placed successfully.")
    except Exception as e:
        print(f"An error occurred during order execution: {e}") 
