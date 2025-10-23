# Measures price volatility

# The wider the band, the more volatile the asset prices as they are k-standard deviations from the middle band (period_n SMA)
#     If 2 standard deviations away, contains 95% of the prices
# Measures whether a price is too high or too low on a relative basis


#Relatively high when close to the upper band
#Relatively cheap when close to the lower band

import matplotlib.pyplot as plt
# Define the Bollinger Bands with 1-sd
upper_1sd, mid_1sd, lower_1sd = talib.BBANDS(bitcoin_data['Close'], 
                                     nbdevup=2,
                                     nbdevdn=2,
                                     timeperiod=20)
# Plot the upper and lower Bollinger Bands 
plt.plot(bitcoin_data['Close'], color='green', label='Price')
plt.plot(upper_1sd, color='tomato', label="Upper 1sd")
plt.plot(lower_1sd, color='tomato', label='Lower 1sd')

# Customize and show the plot
plt.legend(loc='upper left')
plt.title('Bollinger Bands (1sd)')
plt.show()
