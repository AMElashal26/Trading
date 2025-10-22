/* 
ADX Basics: ADX values range from 0 to 100. An ADX below 25 indicates a weak or non-existent trend, while an ADX above 25 suggests a strong trend. It does not indicate the direction of the trend.
Components: ADX is derived from two other indicators: the plus directional index (+DI) and the minus directional index (-DI).
Calculation: ADX can be calculated using high, low, and close prices over a specified period, typically 14 days.
*/


import talib
import matplotlib.pyplot as plt

# fetch Tesla data
try:
    import yfinance as yf
except ImportError:
    raise ImportError("yfinance is required. Install with: pip install yfinance")

# change date range as needed
stock_data = yf.download("TSLA", start="2020-01-01", end="2025-10-22", progress=False)


# Calculate ADX
stock_data['ADX'] = talib.ADX(stock_data['High'], stock_data['Low'], stock_data['Close'])


# Create subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot ADX with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('ADX')
ax2.plot(stock_data['ADX'], color='red')

ax1.set_title('Price and ADX')
plt.show()
