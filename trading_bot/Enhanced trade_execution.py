import ccxt 
from config import api_key, api_secret  

def execute_order(symbol, side, quantity, order_type='MARKET', stop_loss=None):
    binance = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret
    })

    try:
        order_params = {'type': order_type, 'side': side,'amount': quantity}

        if stop_loss:
            # Set stop-loss order parameters (adjust 'stopPrice' as needed)
            order_params['params'] = {
                'stopPrice': stop_loss,  
                'stopPriceType': 'STOP_LOSS' 
            }

        order = binance.create_order(symbol, **order_params)
        print(f"{side} order for {quantity} {symbol} placed successfully.")

    except Exception as e:
        print(f"An error occurred during order execution: {e}") 

