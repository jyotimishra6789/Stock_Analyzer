import yfinance as yf
import heapq
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA"]

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    if not data.empty:
        return {
            "symbol": symbol,
            "open": data["Open"][0],
            "close": data["Close"][0],
        }
    return None

stock_data = [get_stock_data(stock) for stock in stocks]
stock_data = [stock for stock in stock_data if stock]

for stock in stock_data:
    stock["performance"] = ((stock["close"] - stock["open"]) / stock["open"]) * 100

stock_data.sort(key=lambda x: x["performance"], reverse=True)

k = 3

top_gainers = heapq.nlargest(k, stock_data, key=lambda x: x["performance"])
top_losers = heapq.nsmallest(k, stock_data, key=lambda x: x["performance"])

print("\n📈 Top", k, "Performing Stocks:")
for stock in top_gainers:
    print(f"{stock['symbol']} - {stock['performance']:.2f}%")

print("\n📉 Worst", k, "Performing Stocks:")
for stock in top_losers:
    print(f"{stock['symbol']} - {stock['performance']:.2f}%")

symbols = [stock["symbol"] for stock in stock_data]
performance = [stock["performance"] for stock in stock_data]

plt.figure(figsize=(10, 5))
plt.bar(symbols, performance, color=["green" if p > 0 else "red" for p in performance])
plt.xlabel("Stock Symbol")
plt.ylabel("Performance (%)")
plt.title("Stock Performance - Top Gainers & Losers")
plt.axhline(y=0, color="black", linestyle="--")
plt.show()
