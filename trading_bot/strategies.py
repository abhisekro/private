from indicators import calculate_sma, calculate_rsi, calculate_bollinger_bands  
from patterns import detect_doji, detect_bullish_engulfing

def simple_sma_crossover_strategy(df):
    """Strategy: Buy when fast SMA crosses above slow SMA, sell when vice-versa"""

    if df['SMA_20'].iloc[-1] > df['SMA_50'].iloc[-1] and df['SMA_20'].iloc[-2] <= df['SMA_50'].iloc[-2]:
        return 'BUY' 
    elif df['SMA_20'].iloc[-1] < df['SMA_50'].iloc[-1] and df['SMA_20'].iloc[-2] >= df['SMA_50'].iloc[-2]:
        return 'SELL'
    else:
        return 'HOLD'  

def rsi_and_engulfing_strategy(df):
    """Strategy: Buy when RSI is oversold and a bullish engulfing pattern occurs"""

    last_rsi = df['RSI'].iloc[-1]
    last_engulfing = df['bullish_engulfing'].iloc[-1]

    if last_rsi < 30 and last_engulfing > 0: 
        return 'BUY'
    else:
        return 'HOLD'  # You can add a SELL condition here if needed


# Add other strategies as needed...
