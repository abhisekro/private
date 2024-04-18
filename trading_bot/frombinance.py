import os
import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # For optional visualizations
import talib  


# --- API Keys loading ---
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')


# Initialize Binance client
binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret
})

# --- Data Fetching ---
symbol = 'LINK/USDT'
timeframe = '1h' 
limit = 500  # Fetch 500 candlesticks
ohlcv_data = binance.fetch_ohlcv(symbol, timeframe, limit=limit)

df = pd.DataFrame(ohlcv_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamps

# --- Technical Indicators -- (SMA)
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

def rsi(df, period=14):
    
# Relative Strength Index (RSI)
    delta = df['close'].diff()
    gains, losses = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    losses[losses > 0] = 0
    avg_gain = gains.rolling(window=period).mean()
    avg_loss = losses.rolling(window=period).mean()
    rs = abs(avg_gain / avg_loss)
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI'] = rsi(df)

# Bollinger Bands 
def bollinger_bands(df, period=20, std_multiplier=2):
    df['BB_Middle'] = df['close'].rolling(window=period).mean()
    df['BB_Upper'] = df['BB_Middle'] + std_multiplier * df['close'].rolling(window=period).std() 
    df['BB_Lower'] = df['BB_Middle'] - std_multiplier * df['close'].rolling(window=period).std() 
    return df

df = bollinger_bands(df)

# --- Pattern Detection ---
def detect_doji(df):
    doji_threshold = 0.1  # Adjust as needed 
    df['is_doji'] = abs(df['open'] - df['close']) / (df['high'] - df['low']) < doji_threshold
    return df 

df = detect_doji(df)

def detect_bullish_engulfing(df):
    pattern = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close']) 
    df['bullish_engulfing'] = pattern
    return df

df = detect_bullish_engulfing(df)

# --- Analysis (Modify & Expand) ---


def check_support_resistance(df):
    threshold = 0.02  # Adjust this percentage tolerance 

    for i in range(2, len(df)):  # Check from the third candle onwards
        prev_close = df['close'].iloc[i - 1]
        current_close = df['close'].iloc[i]

        # Support Check
        if (df['SMA_20'].iloc[i - 2] < prev_close < df['SMA_20'].iloc[i - 1] < current_close) \
                and (abs(prev_close - df['SMA_20'].iloc[i]) / prev_close <= threshold):  # Price bounces off SMA_20
            print("Potential Support near:", df['SMA_20'].iloc[i])  # Alert

        # Resistance Check (similar logic, reversed)
        if (df['SMA_20'].iloc[i - 2] > prev_close > df['SMA_20'].iloc[i - 1] > current_close) \
                and (abs(prev_close - df['SMA_20'].iloc[i]) / prev_close <= threshold): 
            print("Potential Resistance near:", df['SMA_20'].iloc[i])  # Alert

check_support_resistance(df)

print(df.tail())  # View the most recent data

# ... Add your logic for analyzing indicators, patterns, and making decisions ...
# ... inside your analysis section ...

# --- Optional: Visualization ---
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['close'])
plt.plot(df['timestamp'], df['SMA_20'], label='SMA 20')
plt.plot(df['timestamp'], df['SMA_50'], label='SMA 50')
plt.title('LINK/USDT with SMAs')
plt.legend()
plt.show()
