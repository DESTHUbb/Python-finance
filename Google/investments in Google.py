import pandas as pd
import matplotlib.pyplot as plt

#Next, the historical data from GOOGL is loaded using the yfinance package:

import yfinance as yf
googl = yf.download("GOOGL")

#Then, the necessary variables for the investment model are calculated. For example, you can calculate the daily return and the 50-day moving average:

googl['returns'] = googl['Adj Close'].pct_change()
googl['SMA'] = googl['Adj Close'].rolling(window=50).mean()

#An investment strategy is then defined using the model. For example, you can buy the stock if the current price is above the 50-day moving average and sell it if it is below:

googl['position'] = 0
googl['position'][googl['Adj Close'] > googl['SMA']] = 1
googl['position'][googl['Adj Close'] < googl['SMA']] = -1
googl['position'] = googl['position'].fillna(method='ffill')
googl['strategy'] = googl['position'].shift(1) * googl['returns']

#Finally, the performance of the strategy is evaluated and compared to a buy and hold strategy. For example, you can calculate the cumulative return and graph it:

googl['cumulative_strategy'] = (googl['strategy'] + 1).cumprod()
googl['cumulative_buy_hold'] = (googl['returns'] + 1).cumprod()
plt.plot(googl['cumulative_strategy'])
plt.plot(googl['cumulative_buy_hold'])
plt.legend(['investment strategy', 'Purchase and hold'])
plt.show()
