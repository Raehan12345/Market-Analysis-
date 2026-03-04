import numpy as np
import pandas as pd

def calculate_roll_spread(prices):
    # calculate the price changes
    returns = np.diff(prices)
    
    # calculate the autocovariance of the returns
    # we need the covariance between consecutive price changes
    if len(returns) < 2:
        return np.nan
        
    autocov = np.cov(returns[:-1], returns[1:])[0, 1]
    
    # the roll model assumes negative autocovariance
    # if positive, the spread is effectively zero
    if autocov < 0:
        return 2 * np.sqrt(-autocov)
    else:
        return 0.0