import pandas as pd 
import talib

def detect_doji(df, threshold=0.1):
    df['is_doji'] = abs(df['open'] - df['close']) / (df['high'] - df['low']) < threshold
    return df 

def detect_bullish_engulfing(df):
    pattern = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close']) 
    df['bullish_engulfing'] = pattern
    return df

