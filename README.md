# Stock Price Prediction Using Machine Learning
## 📌 Overview
This project aims to predict stock price movements using machine learning models such as Linear Regression. The model analyze historical stock data and sentiment analysis from social media to generate predictions for future stock price movements.

## 🚀 Features
Sentiment Analysis: Combines sentiment data from Telegram (using Telethon Library) with stock price data.

Historical Stock Data Analysis: To take historical data imported yfinance from python. Utilizes attributes such as Date, open, high, low, close prices, volume, and sentiment scores.

Model: Implements machine learning model and calculated its accuracy and performance.
Key Metrics: Evaluates model performance using metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE), R<sup>2</sup> , Accuracy, Precision, F1-Score score.

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


## 🛠️ How to Run

Preprocess Data:
Ensure both sentiment and stock data are cleaned and merged.
Check for missing values and handle them appropriately.

Train Model:
To train a Linear Regression model, the necessary libraries are imported, and features (Sentiment, Volume, Open, High, Low) and the target (Adj Close) are defined from final_df. The data is split into training (80%) and testing (20%) sets using train_test_split with a fixed random state for reproducibility. A LinearRegression model is then trained on the training set and used to predict Adj Close values for the test set, with the predictions printed for evaluation.

Evaluate Model:
Use metrics such as MSE, MAE, R<sup>2</sup>, Accuracy, Precision, F1-score to assess performance.

Make Predictions:
Pass new data to the trained model to predict stock prices.

## 🔑 Key Results
Result Metric	Linear Regression:

R^2 Score:	0.998	

MSE:	1.05	

MAE:	0.71	

Accuracy: 1.0

Precision: 1.0

F1 Score: 1.0


<img width="590" alt="image" src="https://github.com/user-attachments/assets/3ffd4b33-9345-4c3c-9616-f497cdd6c4eb">


## 💻 Technologies Used
Programming Language: Python

Libraries: Scikit-learn, Pandas, NumPy, Matplotlib/Seaborn for visualization

## 📝 Future Scope
Incorporate deep learning models like LSTMs for time-series analysis.

Expand the sentiment analysis pipeline using natural language processing (NLP) techniques.

Explore additional stock market indicators for feature enhancement.


## 🤝 Contributing
Contributions are welcome! Please create a pull request or raise an issue for any feature suggestions or bug fixes.

## 📞 Contact
Author: Latika Mangla

Email: latikamangla18@gmail.com

GitHub: LatikaMangla18
