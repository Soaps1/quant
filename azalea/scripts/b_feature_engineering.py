import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))  # ← back to quant/
sys.path.insert(0, root_path)

from src.utils import get_stock_data

stock = get_stock_data('AAPL') 
benchmark = get_stock_data('SPY')  # Example ticker

def main():
    # Display the first few rows of the data
    print(df.tail())

if __name__ == "__main__":
    main()