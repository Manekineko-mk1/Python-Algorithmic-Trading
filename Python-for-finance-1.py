import datetime as dt
from matplotlib import style
import pandas_datareader.data as web  # use to grab data from API

# This introduces a simple way to grab a stock data of a predetermined time interval.

# Open - When the stock market opens in the morning for trading, what was the price of one share?
# High - over the course of the trading day, what was the highest value for that day?
# Low - over the course of the trading day, what was the lowest value for that day?
# Close - When the trading day was over, what was the final price?
# Volume - For that day, how many shares were traded?
# Adj Close - Stock split. New shares in a company to existing shareholders in proportion to their current holdings.

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2017, 4, 4)

# df = data frames
df = web.DataReader('TSLA', 'yahoo', start, end)
print(df.tail(6))  # head() only prints first 5 data frames
