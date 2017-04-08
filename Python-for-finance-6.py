import bs4 as bs  # beautifulSoup
import pickle  # serialize python objects (ex save S&P 500 list table)
import requests
import datetime as dt
import os  # uses to create new directory
import pandas as pd
import pandas_datareader.data as web

# This demonstrates how to grab the pricing data from Yahoo, with the tickers we want.


def run():
    # save_sp500_ticker()
    get_data_from_yahoo()


def save_sp500_ticker():
    # 1. Grab source code from Wikipedia
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "html.parser")

    # 2. Find the table of stock data by searching "wikitable sortable" class
    table = soup.find('table', {'class': 'wikitable sortable'})

    # 3. Specific an empty ticker list. Then iterate through the table.
    tickers = []

    # [1:] = for each row, after the header row "tr" ...
    for row in table.findAll('tr')[1:]:
        # since we want the 0th column; the ticker symbols, so ... .text because it's a SOUP obj
        ticker = row.findAll('td')[0].text

        # Getaround for Berkshire Hathaway ticker BRK.A
        mapping = str.maketrans(".", "-")
        ticker = ticker.translate(mapping)

        # This will give us an array of SP500 tickers list
        tickers.append(ticker)

    # 4. Save the list to a file by serializes the Python objects
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


def get_data_from_yahoo(reload_sp500=False):

    # If true, then we grab ticker list from Wikipedia
    if reload_sp500:
        tickers = save_sp500_ticker()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime (2017, 4, 6)

    for ticker in tickers:
        print("Grabbing price data for " + ticker)

        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

    print("Process completed.")

    return

run()
