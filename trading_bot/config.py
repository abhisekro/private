import os

#telegram api
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = 5020266216

# Binance API Credentials (Load from environment variables preferably)
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

if not telegram_bot_token or not api_key or not api_secret:
    raise EnvironmentError("Missing environment variables. Please set TELEGRAM_BOT_TOKEN, BINANCE_API_KEY, and BINANCE_API_SECRET")

from config import telegram_bot_token, api_key, api_secret  
