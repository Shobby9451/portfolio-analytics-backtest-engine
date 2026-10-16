import yaml
import yfinance

# Let's load config/holdings.yaml first

with open("config/holdings.yaml") as f: 
    text = f.read()
    print(text)
    config = yaml.safe_load(text)


# Download one stock's data 

df = yfinance.download("NVDA", config["start_date"], auto_adjust= True)

# Let's see what the DF looks like

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)