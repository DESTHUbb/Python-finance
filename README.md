# ` Python-finance`
## These investment charts can be a useful tool for making informed decisions about your personal finances. It could help you assess the performance of your current investments, identify new investment opportunities, and plan your finances for the long term.

![image](https://user-images.githubusercontent.com/90658763/229385270-027906f4-07bd-4047-885a-1fce05a19456.png)

## ` AMAZON `  
### Based on these variables, an investment strategy is defined based on buying the share if its current price is above the 50-day moving average and selling it if it is below. This is done by assigning values ​​to a column called "position" in the Pandas DataFrame, and then the performance of the strategy is calculated in another column called "strategy".
### ` How does it work?` 
#### Finally, the performance of the strategy is evaluated and compared to a buy and hold strategy for the stock. The two strategies are plotted using matplotlib and the result is shown.
![AMZN](https://user-images.githubusercontent.com/90658763/229384681-4c63d711-f0a3-45fa-a635-b672c5ee8d6f.png)

## ` APPLE `  
### The code is based on historical price information for a stock, specifically Apple Stock (AAPL), using the yfinance Python library to download the historical stock data from Yahoo Finance.
### ` How does it work?` 
#### The necessary variables for the investment model are calculated, which include the daily performance of the share (returns) and the 20-day simple moving average (SMA). Next, an investment strategy based on the model is defined that consists of buying the stock if the current price is above the 20-day moving average and selling it if it is below.
#### And finally, the performance of the investment strategy is evaluated and compared with a "buy and hold" strategy. The evaluation is done by calculating the cumulative performance of both strategies and plotting the corresponding curves on a graph using the matplotlib Python library.
![AAPL](https://user-images.githubusercontent.com/90658763/229386040-f324701c-17de-4c06-8362-56344c2937ea.png)

## ` GOOGLE `  
### The code is based on historical price information for a stock, specifically the Stock of Alphabet Inc., Class A (GOOGL), using the yfinance Python library to download the historical data for the stock from Yahoo Finance
### ` How does it work?` 
#### The necessary variables for the investment model are calculated, which include the daily performance of the share (returns) and the 50-day simple moving average (SMA). Next, an investment strategy is defined based on the model that consists of buying the stock if the current price is above the 50-day moving average and selling it if it is below.
#### The performance of the investment strategy is evaluated and compared to a "buy and hold" strategy. The evaluation is done by calculating the cumulative performance of both strategies and plotting the corresponding curves on a graph using the matplotlib Python library.
![googl](https://user-images.githubusercontent.com/90658763/229386112-3a6eb66d-5d39-4068-af2a-d784383bed04.png)

## `MICROSOFT`
### The code is based on loading historical stock price data for Microsoft (MSFT) using the yfinance package, calculating the daily return and the 50-day moving average, defining an investment strategy based on the model, and evaluating the performance of the strategy compared to a buy and hold strategy. Specifically:

###  1- `The yfinance package is used to load historical data for MSFT.` 
###  2- `The daily return and 50-day moving average of the adjusted closing prices are calculated.` 
###  3- `An investment strategy is defined based on the moving average. If the current price is above the 50-day moving average, the stock is bought, and if it is below, the stock is sold.` 
###  4- `The performance of the investment strategy is evaluated by calculating the cumulative return and comparing it to the cumulative return of a buy and hold strategy.`
###  5- `The cumulative return of the investment strategy and the buy and hold strategy are plotted using the matplotlib library.` 
![MSFT](https://user-images.githubusercontent.com/90658763/229386203-aa45db7d-4390-4547-9996-f23ba9becc69.png)

## `It is important to note that in some cases the model may not be accurate due to market volatility and other external factors, and that past results do not guarantee future results !!!` 
## Source of information
https://pypi.org/project/yfinance/
