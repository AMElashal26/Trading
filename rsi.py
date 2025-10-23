/* RSI Interpretation:

RSI > 70: Indicates an overbought market, suggesting the asset may be overvalued and the price could reverse.
RSI < 30: Indicates an oversold market, suggesting the asset may be undervalued and the price could rally.
RSI Calculation:

Formula: ( RSI = 100 - \frac{100}{1 + RS} )
RS (Relative Strength) is the average of upward price changes divided by the average of downward price changes over a chosen period. 
*/

# Calculate RSI with the default time period
stock_data['RSI_14'] = talib.RSI(stock_data['Close'])

# Calculate RSI with a time period of 21
stock_data['RSI_21'] = talib.RSI(stock_data['Close'], timeperiod=21)

# Print the last five rows
print(stock_data.tail())

# Calculate RSI
stock_data['RSI'] = talib.RSI(stock_data['Close'])

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)
# Plot RSI with the price
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('RSI')
ax2.plot(stock_data['RSI'], color='orangered')

ax1.set_title('Price and RSI')
plt.show()
