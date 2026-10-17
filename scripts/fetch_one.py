import sqlite3

import yaml
import yfinance

# Let's load config/holdings.yaml first

with open("config/holdings.yaml") as f: 
    text = f.read()
    print(text)
    config = yaml.safe_load(text)


# Download all stocks data


for holding in config["holdings"]:
    df = yfinance.download(holding["ticker"], config["start_date"], auto_adjust = True)
    df.columns = df.columns.get_level_values(0)
    conn = sqlite3.connect("data/portfolio.db")
    for date, row in df.iterrows():
        conn.execute(
            "INSERT OR REPLACE INTO prices (ticker, date, close, volume) VALUES ( ?, ?, ?, ?)",
       (holding["ticker"], date.strftime("%Y-%m-%d"), float(row["Close"]), int(row["Volume"])))
    conn.commit()
    conn.close()
    print(df.head())
    print(df.tail())
    print(df.columns)
    print(df.shape)
