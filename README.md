# Stock Price Prediction Using Machine Learning
## 📌 Overview
This project aims to predict stock price movements using machine learning models such as Linear Regression. The model analyze historical stock data and sentiment analysis from social media to generate predictions for future stock price movements.

## 🚀 Features
Sentiment Analysis: Combines sentiment data from Telegram (using Telethon Library) with stock price data.
Historical Stock Data Analysis: To take historical data imported yfinance from python. Utilizes attributes such as Date, open, high, low, close prices, volume, and sentiment scores.
Model: Implements machine learning model and calculated its accuracy and performance.
Key Metrics: Evaluates model performance using metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE), and R^2 score.
Predictive Capabilities: Provides insights into future stock price movements.

## 📂 Dataset
Sentiment Data: Scraped data from telegram groups/channels. 
Columns: Message_ID, Sender_ID, Date, Message_Text, Cleaned_Text, Sentiment.
Contains social media messages with preprocessed sentiment scores.

Stock Data: Imported from yfinance library from python 
Columns: Date, Open, High, Low, Close, Adj Close, Volume.
Historical stock prices for the selected ticker (e.g., AAPL).

Merged Dataset:
Combines sentiment data and stock data using the Date column.

## ⚙️ Installation

📊 Implemented Model
Linear Regression
Simple and interpretable model for regression tasks.

Metrics:
R^2 Score: 0.998\\
MSE: 1.05\\
MAE: 0.71\\
Accuracy: 1.0\\
Precision: 1.0\\
F1 Score: 1.0

## 🛠️ How to Run

Preprocess Data:
Ensure both sentiment and stock data are cleaned and merged.
Check for missing values and handle them appropriately.

Train Model:
Use the script below to train the Linear Regression model:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

Features and Target
features = final_df[['Sentiment', 'Volume', 'Open', 'High', 'Low']]
target = final_df['Adj Close']

Split Data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

Train Model
model = LinearRegression()
model.fit(X_train, y_train)

Evaluate
predictions = model.predict(X_test)
print(predictions)

Evaluate Model:
Use metrics such as MSE, MAE, and R^2 to assess performance.

Make Predictions:
Pass new data to the trained model to predict stock prices.

## 🔑 Key Results
Result Metric	Linear Regression
R^2 Score:	0.998	
MSE:	1.05	
MAE:	0.71	
Accuracy: 1.0
Precision: 1.0
F1 Score: 1.0

## 💻 Technologies Used
Programming Language: Python
Libraries: Scikit-learn, Pandas, NumPy, Matplotlib/Seaborn for visualization

## 📝 Future Scope
Incorporate deep learning models like LSTMs for time-series analysis.
Expand the sentiment analysis pipeline using natural language processing (NLP) techniques.
Explore additional stock market indicators for feature enhancement.


🤝 Contributing
Contributions are welcome! Please create a pull request or raise an issue for any feature suggestions or bug fixes.

📞 Contact
Author: Latika Mangla
Email: latikamangla18@gmail.com
GitHub: 
