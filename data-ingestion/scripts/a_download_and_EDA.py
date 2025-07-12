import sys
import os
import pandas as pd

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))  # ← back to quant/
sys.path.insert(0, root_path)

from src.utils import get_stock_data
from src.utils import calculate_daily_returns
from src.utils import sma, ema, momentum, volatility, rolling_range, rsi
from src.features import print_hello_world
from z_helper_functions import greeting


def get_stock_signals(ticker):
    # Get raw stock data
    raw_data = get_stock_data(ticker)
    
    # Calculate daily returns
    returns = calculate_daily_returns(raw_data)

    # Create a DataFrame for signals
    signals = pd.DataFrame(index=raw_data.index)
    signals['returns'] = returns
    signals['sma_20'] = sma(raw_data['Close'], 20)
    signals['ema_20'] = ema(raw_data['Close'], 20)
    signals['mom_5d'] = momentum(raw_data['Close'], 5)
    signals['vol_10d'] = volatility(raw_data['Close'], 10)
    signals['range_20d'] = rolling_range(raw_data['Close'], 20)
    signals['rsi_14d'] = rsi(raw_data['Close'], 14)
    
    signals.dropna(inplace=True)  # Drop rows with NaN values after calculations
    return raw_data, signals

def main():
    greeting()
    print_hello_world()  # Call the function to print "Hello, world!"
    data, signals = get_stock_signals('AAPL')  # Example ticker
    print(data.head())  # Display the first few rows of the loaded data
    print(signals.tail())  # Display the first few rows of signals

if __name__ == "__main__":
    main()
