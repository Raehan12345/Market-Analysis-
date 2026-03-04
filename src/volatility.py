import numpy as np
import pandas as pd

def calculate_historical_volatility(prices, window=252):
    # calculate logarithmic returns for the price series
    returns = np.log(prices / prices.shift(1))
    
    # calculate the rolling standard deviation
    # multiply by the square root of the window to annualize it
    volatility = returns.rolling(window=window).std() * np.sqrt(252)
    
    return volatility

def estimate_parkinson_volatility(high, low, window=252):
    # parkinson volatility uses high and low prices for a better intraday estimate
    constant = 1.0 / (4.0 * np.log(2.0))
    rs = constant * (np.log(high / low) ** 2)
    
    # calculate rolling mean and annualize
    volatility = np.sqrt(rs.rolling(window=window).mean() * 252)
    return volatility