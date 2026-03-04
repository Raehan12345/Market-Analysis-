import yfinance as yf
import pandas as pd

def fetch_market_data(ticker_symbol, start_date, end_date, interval="1m"):
    # fetch historical data using yfinance
    # using 1-minute intervals since free tick data is heavily restricted
    ticker = yf.Ticker(ticker_symbol)
    df = ticker.history(start=start_date, end=end_date, interval=interval)
    
    # reset index to make datetime a standard column
    df = df.reset_index()
    return df