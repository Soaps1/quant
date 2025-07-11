import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))  # ← back to quant/
sys.path.insert(0, root_path)

from src.utils import load_data
from src.utils import get_stock_data

def load_stock_data(ticker):
    stock_data = get_stock_data(ticker)
    return stock_data

def main():
    #data = load_data(r"C:\Users\Schalk\OneDrive - Columbia Business School\2025\quant\stock-data.csv")
    data = load_stock_data("AAPL")  # Example ticker
    print(data.head())  # Display the first few rows of the loaded data

if __name__ == "__main__":
    main()
