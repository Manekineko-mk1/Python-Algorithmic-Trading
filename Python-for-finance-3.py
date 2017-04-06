import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

# This demonstrates more advanced techniques about data manipulation and visualization.


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

    # print(df.tail())

    return df


def visualization(data_frame):
    # subplot2grid((x by y size), (starting coordinates), rowspan=, colspan=)
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    # sharex allows ax2 will always align its x axis with whatever ax1's is, and visa-versa
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    ax1.plot(data_frame.index, data_frame['Adj Close'])
    ax1.plot(data_frame.index, data_frame['100ma'])
    ax2.bar(data_frame.index, data_frame['Volume'])

    plt.show()

    return


run()