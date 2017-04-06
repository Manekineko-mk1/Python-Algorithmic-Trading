import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web

# This demonstrates more advanced techniques about using candlestick/OHLC graph for visualization.

style.use('ggplot')


def run():
    data = table_manipulation()
    visualization(data)
    return


def table_manipulation():
    style.use('ggplot')
    df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

    # 100ma = 100 moving average, today's price + 99 prior price; shows up/downtrend
    # Take 100 prior frames, take its mean; if no not enough rolls, take means so far
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)  # drop the data frame(roll) if the data needed is missing

    # Resample: resample uniform or nonuniform data to new fixed rate (change sample rate)
    # For stock data, we currently have daily data and we will resample it to 10-day data.

    # Step 1: Create new data frame
    df_ohlc = df['Adj Close'].resample('10D').ohlc()  # other options are mean(), sum()

    global df_volume
    df_volume = df['Volume'].resample('10D').sum()

    # Step 2: Move table data to matplotlib, so we can graph the OHLC
    # Matplotlib requires dates & end dates in mdates format
    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

    return df_ohlc.values


def visualization(df_ohlc):
    # subplot2grid((x by y size), (starting coordinates), rowspan=, colspan=)
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    # converts the axis from the raw mdate numbers to dates
    ax1.xaxis_date()
    # sharex allows ax2 will always align its x axis with whatever ax1's is, and visa-versa
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    candlestick_ohlc(ax1, df_ohlc, width=2, colorup='g')

    # fill_between(x, y, starting_point)
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

    plt.show()

    return


run()