import yfinance as yf

stock_data = yf.download('AAPL',start='2010-01-01', end='2024-02-29')

print(stock_data)
