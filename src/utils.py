import pandas as pd
import yfinance as yf

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def get_stock_data(ticker):
    stock_data = yf.download(ticker, period="20y", interval="1d", auto_adjust=True)
    return stock_data

def calculate_daily_returns(stock_data):
    return stock_data['Close'].pct_change().dropna()

# 1. Simple moving average (SMA)
def sma(series, window):
    return series.rolling(window).mean()

# 2. Exponential moving average (EMA)
def ema(series, window):
    return series.ewm(span=window, adjust=False).mean()

# 3. Momentum (N-day return)
def momentum(series, window):
    return series.pct_change(periods=window)

# 4. Volatility (rolling std of daily returns)
def volatility(series, window):
    return series.pct_change().rolling(window).std()

# 5. Rolling range (high-low over window)
def rolling_range(series, window):
    return series.rolling(window).max() - series.rolling(window).min()

# 6. Relative Strength Index (RSI)
def rsi(series, window):
    delta = series.diff()
    gain  = delta.clip(lower=0)
    loss  = -delta.clip(upper=0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
