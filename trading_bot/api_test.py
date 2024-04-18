import os
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_API_SECRET')
print(f"Retrieved API Key: {api_key}")  # Don't print the actual key for security
print(f"Retrieved API Secret: {api_secret[:5]}...")  # Mask the secret
