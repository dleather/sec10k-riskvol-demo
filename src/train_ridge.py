import pandas as pd, yfinance as yf, sys, numpy as np
from sklearn.linear_model import Ridge

tickers = ["AAPL","MSFT",...]  # align with filings
vols = []
for t in tickers:
        px = yf.download(t, period="1y")["Adj Close"].pct_change()
            vols.append(px.rolling(63).std().iloc[-1])
            y = np.array(vols)

            X = pd.read_csv("data/features.csv").values
            print("R²:", Ridge().fit(X, y).score(X, y))

