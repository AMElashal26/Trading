
import bt
# Get price data by the stock ticker
price_data = bt.get('aapl', start='2019-11-1', end='2020-12-1')

# Calculate the SMA
sma = price_data.rolling(20).mean()
