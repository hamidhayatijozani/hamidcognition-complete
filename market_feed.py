# data/market_feed.py
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_candles(symbol, timeframe, n):
    """
    دریافت داده‌های بازار
    در محیط وب از yfinance استفاده می‌کنیم چون MT5 نیاز به نصب کلاینت دارد
    """
    # تبدیل تایم‌فریم به فرمت yfinance
    yf_interval = "1m"
    if timeframe == "M5": yf_interval = "5m"
    if timeframe == "M15": yf_interval = "15m"
    
    try:
        ticker = yf.Ticker(f"{symbol}=X")
        df = ticker.history(period="5d", interval=yf_interval)
        if df.empty:
            raise RuntimeError("No market data received")
        
        df = df.tail(n).copy()
        df.reset_index(inplace=True)
        df.rename(columns={
            "Datetime": "time",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "tick_volume"
        }, inplace=True)
        
        return df[["time", "open", "high", "low", "close", "tick_volume"]]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
