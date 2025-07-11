import yfinance as yf

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        return a
    
def get_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data for a given ticker and time period using yfinance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
        pandas.DataFrame: DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def calculate_moving_average(data, window):
    """
    Calculates the moving average of a stock's closing prices.

    Args:
        data (pandas.DataFrame): DataFrame containing stock data with a 'Close' column.
        window (int): The number of periods over which to calculate the moving average.
    
    Returns:
        pandas.Series: Series containing the moving average values.
    """
    return data['Close'].rolling(window=window).mean()

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    """
    Calculates Bollinger Bands for a stock's closing prices.

    Args:
        data (pandas.DataFrame): DataFrame containing stock data with a 'Close' column.
        window (int): The number of periods for the moving average.
        num_std_dev (int): The number of standard deviations for the bands.
    
    Returns:
        pandas.DataFrame: DataFrame containing the moving average, upper band, and lower band.
    """
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()
    
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)
    
    return pd.DataFrame({
        'Moving Average': rolling_mean,
        'Upper Band': upper_band,
        'Lower Band': lower_band
    })

def calculate_rsi(data, window=14):
    """
    Calculates the Relative Strength Index (RSI) for a stock's closing prices.

    Args:
        data (pandas.DataFrame): DataFrame containing stock data with a 'Close' column.
        window (int): The number of periods for the RSI calculation.
    
    Returns:
        pandas.Series: Series containing the RSI values.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi


# write a standalone function to check perfect squares
def is_perfect_square(n):
    """
    Checks if a given integer n is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

#
def generate_random_number(start=0, end=100):
    """
    Generates a random integer between start and end (inclusive).

    Args:
        start (int): The lower bound of the range.
        end (int): The upper bound of the range.

    Returns:
        int: A randomly generated integer within the specified range.
    """
    return random.randint(start, end)
