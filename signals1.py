
import bt
import talib

# Get price data by the stock ticker
price_data = bt.get('aapl', start='2019-11-1', end='2020-12-1')

# Calculate the SMA
sma = price_data.rolling(20).mean()

# Define the strategy
bt_strategy = bt.Strategy('AboveSMA', 
                          [bt.algos.SelectWhere(price_data > sma),
                           bt.algos.WeighEqually(),
                           bt.algos.Rebalance()])
