import os
from binance.client import Client

# Load API keys from environment variables (the secure way)
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')

# Create the Binance client
client = Client(api_key, api_secret)

# Test connection
try:
    info = client.get_account()
    print("Connected to Binance successfully!")
except Exception as e:
    print("Connection failed. Error:", e)
