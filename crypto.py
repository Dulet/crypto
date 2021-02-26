import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import random
import json

table = pd.read_html("https://finance.yahoo.com/cryptocurrencies?offset=0&count=100")
split = list(table[0]["Symbol"])
print(split)

with open("crypto.json", "w") as f:
    json.dump(split, f)