# stock-market-prediction

Stock market that predict the closing price for a stock. Which use the free financial stock market data from Yahoo financial. With a model selection train and test model to train the given data from Yahoo financial.
On a linear regression model. 

NOTE** Stock.py was to test if yfinancial works, from the download and see if the data was store by printing it out**

# what I learned

- How to implentment the yfinancial in python
    - Downloading the stock market data assocaiting to the stock I'm look at which is APPLE stock.
    - cleaning that data by droping the NA/Null

- using flask libraries
    - Flask
    - request
    - jsonify

- How to configure postman host associate with this python project
    - by writing in json to send the request from it to the application of the (open price, high price, low price, volume of the stock)
    - getting back a prediction of the closing prices of that date
