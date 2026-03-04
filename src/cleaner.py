import pandas as pd
import numpy as np

def clean_tick_data(df, price_col='Close', z_threshold=3.0):
    # drop rows with missing values to ensure clean calculations
    df_cleaned = df.dropna().copy()
    
    # calculate z-scores to identify extreme price spikes or bad data points
    mean_price = df_cleaned[price_col].mean()
    std_price = df_cleaned[price_col].std()
    z_scores = np.abs((df_cleaned[price_col] - mean_price) / std_price)
    
    # filter out rows where the z-score exceeds our threshold
    df_cleaned = df_cleaned[z_scores < z_threshold]
    
    return df_cleaned