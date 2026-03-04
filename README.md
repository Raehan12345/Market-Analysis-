# Market Data Analysis

A quantitative research project focused on processing high-frequency market data and analyzing market microstructure. 

## Objective
Download historical market data from free sources. Clean and process tick data. Calculate volatility surfaces. Analyze order book dynamics. Find patterns in market microstructure. Document findings in Jupyter notebooks.

## Project Structure

The repository is organized into three main directories to separate core logic from data and analysis:

* `data/`: Local storage for financial data. 
  * `raw/`: Unaltered data downloaded directly from the source.
  * `processed/`: Cleaned data with outliers removed, ready for modeling.
* `notebooks/`: Jupyter notebooks containing exploratory data analysis and documented findings.
* `src/`: Modular Python scripts containing the core quantitative functions.

### Analysis Pipeline

The analysis is broken down into five sequential Jupyter notebooks:

1. **01_data_download.ipynb**: Fetches 1-minute historical data using Yahoo Finance.
2. **02_tick_cleaning.ipynb**: Removes missing values and filters extreme price spikes using a z-score threshold.
3. **03_volatility_surface.ipynb**: Calculates rolling historical volatility and Parkinson high/low volatility estimates.
4. **04_order_book_dynamics.ipynb**: Approximates order flow direction and calculates rolling volume imbalances.
5. **05_microstructure_patterns.ipynb**: Applies the Roll model to estimate effective bid/ask spreads from trade prices.

## Setup Instructions

These instructions assume you are running a Windows environment. 

**1. Clone the repository**
```powershell
# clone the repo to your local machine
git clone [https://github.com/yourusername/market_data_analysis.git](https://github.com/yourusername/market_data_analysis.git)
cd market_data_analysis