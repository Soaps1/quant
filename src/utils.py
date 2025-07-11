import pandas as pd
import yfinance as yf

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def get_stock_data(ticker):
    stock_data = yf.download(ticker, period="20y", interval="1d", auto_adjust=True)
    return stock_data