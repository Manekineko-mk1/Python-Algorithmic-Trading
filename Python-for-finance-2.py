import datetime as dt
from matplotlib import style
import pandas_datareader.data as web  # use to grab data from API

import pandas as pd
import matplotlib.pyplot as plt

# This demonstrates how to handle stock data with Panda and visualize the data with Matplotlib

# Open - When the stock market opens in the morning for trading, what was the price of one share?
# High - over the course of the trading day, what was the highest value for that day?
# Low - over the course of the trading day, what was the lowest value for that day?
# Close - When the trading day was over, what was the final price?
# Volume - For that day, how many shares were traded?
# Adj Close - Stock split. New shares in a company to existing shareholders in proportion to their current holdings.


def get_data():
    # get stock data from Yahoo, output it as csv file
    style.use('ggplot')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 4, 4)

    # df = data frames
    df = web.DataReader('TSLA', 'yahoo', start, end)
    df.to_csv('tsla.csv')
    return


def analysis_csv():
    df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
    # print(df.head())
    # To plot specific column use df ['Column_Name'].plot() ... or mult. columns using [['a','b']]
    df[['Open', 'High', 'Close']].tail(90).plot()
    plt.show()
    return


def run():
    get_data()
    analysis_csv()
    return

run()





