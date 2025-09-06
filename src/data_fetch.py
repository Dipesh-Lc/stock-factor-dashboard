import yfinance as yf
import pandas as pd

tickers = ["AAPL","MSFT","AMZN","NVDA","TSLA","JPM","BAC","XOM","CVX","PG","KO","DIS"]

def download_prices(tickers, start="2019-01-01", end=None):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    return data

if __name__ == "__main__":
    prices = download_prices(tickers)
    prices.to_csv("data/raw/prices_all.csv")
    print("Saved data/raw/prices_all.csv")
