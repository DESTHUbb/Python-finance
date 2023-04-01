import pandas as pd
import matplotlib.pyplot as plt

#The historical data of a stock from the stock market can then be loaded. For example, you can use the yfinance package to get Apple's historical stock prices (AAPL):

import yfinance as yf 
aapl = yf.download("AAPL")

#Then, the variables needed for the investment model can be calculated. For example, you can calculate the daily return and the 20-day moving average:

aapl['returns']= aapl['Adj Close'].pct_change()
aapl['SMA']= aapl['Adj Close'].rolling(window=20).mean()

#Afterwards, an investment strategy can be defined using the model. For example, you can buy the stock if the current price is above the 20-day moving average and sell it if it is below:

aapl['position'] = 0
aapl['position'][aapl['Adj Close'] > aapl['SMA']] = 1
aapl['position'][aapl['Adj Close'] < aapl['SMA']] = -1
aapl['position'] = aapl['position'].fillna(method='ffill')
aapl['strategy'] = aapl['position'].shift(1) * aapl['returns']

#Finally, the performance of the strategy can be evaluated and compared to a buy and hold strategy. For example, you can calculate the cumulative return and graph it:

aapl['cumulative_strategy'] = (aapl['strategy'] + 1).cumprod()
aapl['cumulative_buy_hold'] = (aapl['returns'] + 1).cumprod()
plt.plot(aapl['cumulative_strategy'])
plt.plot(aapl['cumulative_buy_hold'])
plt.legend(['investment strategy', 'Purchase and hold'])
plt.show()

