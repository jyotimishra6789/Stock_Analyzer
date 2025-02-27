# 📊 Top k Performing Stocks - Stock Analysis using Python

## 🚀 Overview
This project analyzes the daily performance of selected stocks using **Yahoo Finance**, calculates their percentage changes, and identifies the **top k gainers and losers** using **Heaps (Min-Heap & Max-Heap)**. The results are visualized using a bar chart.

## 🛠️ Technologies Used
- **Python** (Core programming language)
- **yfinance** (Fetches real-time stock data)
- **pandas** (Data handling and manipulation)
- **heapq** (Efficient top k selection)
- **matplotlib** (Data visualization)

## 📌 Features
- Fetches **real-time stock data** (Opening & Closing prices)
- Computes **percentage change** for each stock
- Uses **Heaps** to quickly find **top k gainers & losers**
- Displays results in the console
- Visualizes stock performance using a **bar chart**


## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-analysis.git
   cd stock-analysis
   ```
2. **Install dependencies:**
   ```bash
   pip install yfinance pandas matplotlib
   ```

## 📈 Usage
Run the Python script to fetch stock data, compute performance, and visualize results.
```bash
python stock_analysis.py
```

## 📊 Example Output
```
📈 Top 3 Performing Stocks:
TSLA - 2.45%
NVDA - 1.80%
AAPL - 1.25%

📉 Worst 3 Performing Stocks:
AMZN - (-1.20)%
GOOGL - (-0.80)%
META - (-0.50)%
```
✅ A **bar chart** will also be displayed, showing stock performance.

## 📜 Code Explanation
1. Fetch stock data for **selected stocks**.
2. Calculate **daily percentage change**.
3. Use **Max-Heap** to find **top k gainers**.
4. Use **Min-Heap** to find **top k losers**.
5. Display results & generate **bar chart visualization**.

## 📌 Customization
- Modify the **stock symbols** in `stocks` list.
- Change **number of top stocks (k)** in `k = 3`.
- Adjust **date range** in `stock.history(period="1d")`.

## 🤝 Contributing
Feel free to **fork** this repo and submit **pull requests** with improvements! 🚀

## 📜 License
This project is licensed under the **MIT License**.

---
💡 **Happy Coding & Investing!** 📈🚀

