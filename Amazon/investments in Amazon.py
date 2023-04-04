import pandas as pd
import matplotlib.pyplot as plt

#Next, the historical data from AMZN is loaded using the yfinance package:

import yfinance as yf
amzn = yf.download("AMZN")

#Then, the necessary variables for the investment model are calculated. For example, you can calculate the daily return and the 50-day moving average:

amzn['returns'] = amzn['Adj Close'].pct_change()
amzn['SMA'] = amzn['Adj Close'].rolling(window=50).mean()

#An investment strategy is then defined using the model. For example, you can buy the stock if the current price is above the 50-day moving average and sell it if it is below:

amzn['position'] = 0
amzn.loc[amzn['Adj Close'] > amzn['SMA'], 'position'] = 1
amzn.loc[amzn['Adj Close'] < amzn['SMA'], 'position'] = -1
amzn['position'] = amzn['position'].fillna(method='ffill')
amzn['strategy'] = amzn['position'].shift(1) * amzn['returns']

#Finally, the performance of the strategy is evaluated and compared to a buy and hold strategy. For example, you can calculate the cumulative return and graph it:

amzn['cumulative_strategy'] = (amzn['strategy'] + 1).cumprod()
amzn['cumulative_buy_hold'] = (amzn['returns'] + 1).cumprod()
plt.plot(amzn['cumulative_strategy'])
plt.plot(amzn['cumulative_buy_hold'])
plt.legend(['investment strategy', 'Purchase and hold'])
plt.show()
