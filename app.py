from flask import Flask, request, jsonify
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


def fetch_and_preprocess_stock_data(symbol):
    stock_data = yf.download(symbol, start='2010-01-01', end='2024-06-28')

    stock_data_cleaned = stock_data.dropna()

    return stock_data_cleaned


stock_data_cleaned = fetch_and_preprocess_stock_data('AAPL')

X = stock_data_cleaned[['Open', 'High', 'Low', 'Volume']]
y = stock_data_cleaned['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    stock_features = data['features']
    predicted_price = model.predict([stock_features])[0]
    response = {'predicted_price': predicted_price}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
