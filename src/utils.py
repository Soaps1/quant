import math

# Calculates the simple moving average of a list of prices
def simple_moving_average(prices, window):
    return [sum(prices[i-window+1:i+1])/window for i in range(window-1, len(prices))]

# Calculates the exponential moving average of a list of prices
def exponential_moving_average(prices, window):
    ema = []
    k = 2 / (window + 1)
    for i, price in enumerate(prices):
        if i == 0:
            ema.append(price)
        else:
            ema.append(price * k + ema[-1] * (1 - k))
    return ema

# Calculates daily returns from a list of prices
def daily_returns(prices):
    return [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]

# Calculates log returns from a list of prices
def log_returns(prices):
    return [math.log(prices[i] / prices[i-1]) for i in range(1, len(prices))]

# Calculates the volatility (standard deviation) of returns
def volatility(returns):
    mean = sum(returns) / len(returns)
    return (sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)) ** 0.5

# Calculates the Sharpe ratio given returns and risk-free rate
def sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = [r - risk_free_rate for r in returns]
    avg_excess = sum(excess_returns) / len(excess_returns)
    vol = volatility(excess_returns)
    return avg_excess / vol if vol != 0 else 0

# Normalizes a list of values to have mean 0 and std 1
def zscore(values):
    mean = sum(values) / len(values)
    std = (sum((v - mean) ** 2 for v in values) / (len(values) - 1)) ** 0.5
    return [(v - mean) / std for v in values]