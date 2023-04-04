import pandas as pd
import matplotlib.pyplot as plt

#Next, the historical data from MSFT is loaded using the yfinance package:

import yfinance as yf
msft = yf.download("MSFT")

#Then, the necessary variables for the investment model are calculated. For example, you can calculate the daily return and the 50-day moving average:

msft['returns'] = msft['Adj Close'].pct_change()
msft['SMA'] = msft['Adj Close'].rolling(window=50).mean()

#An investment strategy is then defined using the model. For example, you can buy the stock if the current price is above the 50-day moving average and sell it if it is below:

msft['position'] = 0
msft.loc[msft['Adj Close'] > msft['SMA'], 'position'] = 1
msft.loc[msft['Adj Close'] < msft['SMA'], 'position'] = -1
msft['position'] = msft['position'].fillna(method='ffill')
msft['strategy'] = msft['position'].shift(1) * msft['returns']

#Finally, the performance of the strategy is evaluated and compared to a buy and hold strategy. For example, you can calculate the cumulative return and graph it:

msft['cumulative_strategy'] = (msft['strategy'] + 1).cumprod()
msft['cumulative_buy_hold'] = (msft['returns'] + 1).cumprod()
plt.plot(msft['cumulative_strategy'])
plt.plot(msft['cumulative_buy_hold'])
plt.legend(['investment strategy', 'Purchase and hold'])
plt.show()
