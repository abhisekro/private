import pandas as pd
import matplotlib.pyplot as plt 

from config import telegram_send_alert  # Assuming Telegram setup is here
from utils import fetch_ohlcv
from indicators import calculate_sma, calculate_rsi, calculate_bollinger_bands
from patterns import detect_doji, detect_bullish_engulfing

# Configuration
symbol = 'LINK/USDT'
timeframe = '1h' 
limit = 500 

# Data Fetching
df = fetch_ohlcv(symbol, timeframe, limit)

# Indicator Calculation
df = calculate_sma(df, period=20)
df = calculate_sma(df, period=50)
df = calculate_rsi(df)
df = calculate_bollinger_bands(df)


# Support/Resistance Analysis
check_support_resistance(df) 

def check_support_resistance(df, tolerance=0.02):
    """Checks for potential support and resistance levels based on price bounces 
       off moving averages.

    Args:
        df (pandas.DataFrame): The DataFrame containing OHLCV data and SMAs.
        tolerance (float, optional): Percentage tolerance for price variations 
                                     around the moving average. Defaults to 0.02.
    """

    for i in range(len(df) - 2, 1, -1):  # Iterate from the most recent data backwards
        for sma_period in [20, 50]:  # Check common SMA periods
            sma_name = 'SMA_' + str(sma_period)

            # Support Check
            if (df[sma_name].iloc[i - 2] < df['close'].iloc[i - 1] < df[sma_name].iloc[i - 1] < df['close'].iloc[i]) and \
               (abs(df['close'].iloc[i - 1] - df[sma_name].iloc[i]) / df['close'].iloc[i - 1] <= tolerance):
                print(f"Potential Support near: {df[sma_name].iloc[i]} (SMA {sma_period})")

            # Resistance Check
            if (df[sma_name].iloc[i - 2] > df['close'].iloc[i - 1] > df[sma_name].iloc[i - 1] > df['close'].iloc[i]) and \
               (abs(df['close'].iloc[i - 1] - df[sma_name].iloc[i]) / df['close'].iloc[i - 1] <= tolerance):
                print(f"Potential Resistance near: {df[sma_name].iloc[i]} (SMA {sma_period})")


# Pattern Detection
df = detect_doji(df)
df = detect_bullish_engulfing(df)

# Analysis (Modify & Expand)
def analyze_data(data):
    # ... your analysis logic, including check_support_resistance  ...

# Execution
analyze_data(df.copy())  # Pass a copy to preserve original data

print(df.tail()) 

# ... Rest of your logic for trading decisions and alerts ...
