import bs4 as bs  # beautifulSoup
import pickle  # serialize python objects (ex save S&P 500 list table)
import requests

# This demonstrates how to grab large stock data from Wikipedia, then work on all of those data at once.

def run():
    save_sp500_ticker()


def save_sp500_ticker():
    # 1. Grab source code from Wikipedia
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "html.parser")

    # 2. Find the table of stock data by searching "wikitable sortable" class
    table = soup.find('table', {'class':'wikitable sortable'})

    # 3. Specific an empty ticker list. Then iterate through the table.
    tickers = []

    # [1:] = for each row, after the header row "tr" ...
    for row in table.findAll('tr')[1:]:
        # since we want the 0th column; the ticker symbols, so ... .text because it's a SOUP obj
        ticker = row.findAll('td')[0].text

        # This will give us an array of SP500 tickers list
        tickers.append(ticker)

    # 4. Save the list to a file by serializes the Python objects
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

run()