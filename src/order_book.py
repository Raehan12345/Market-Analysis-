import pandas as pd

def calculate_volume_imbalance(up_volume, down_volume):
    # compute the ratio of upward volume to total volume
    # values near 1 indicate strong buying pressure and values near 0 indicate selling
    total_volume = up_volume + down_volume
    
    # avoid division by zero errors by replacing zeros with a small number
    total_volume = total_volume.replace(0, 1e-9)
    imbalance = up_volume / total_volume
    
    return imbalance

def approximate_order_flow(df):
    # approximate order flow direction using price changes
    # if close is higher than open, we classify volume as buyer initiated
    buyer_volume = df['Volume'].where(df['Close'] > df['Open'], 0)
    seller_volume = df['Volume'].where(df['Close'] < df['Open'], 0)
    
    return buyer_volume, seller_volume