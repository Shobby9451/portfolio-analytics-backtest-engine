import sqlite3

conn = sqlite3.connect("data/portfolio.db")

rows = conn.execute("SELECT ticker, COUNT(*) FROM prices GROUP BY ticker;").fetchall()

print(rows)
