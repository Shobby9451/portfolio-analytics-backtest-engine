import sqlite3

conn = sqlite3.connect("data/portfolio.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS prices (
    ticker TEXT,
    date TEXT,
    close REAL,
    volume INTEGER,
    PRIMARY KEY (ticker, date)
)
""")
conn.commit()
conn.close()
