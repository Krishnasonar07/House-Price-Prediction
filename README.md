# 🏠 House Price Prediction using Linear Regression (NumPy)

This project implements a basic **linear regression model from scratch using NumPy** to predict house prices based on historical data.

## 📂 Project Structure

├── Housing.csv # Feature data (independent variables)<br>
├── price.csv # Target values (house prices)<br>
├── house_price_predictor.py # Python script (main logic)<br>
└── README.md # Project documentation


## 🚀 How It Works

This project uses the **Normal Equation** method for linear regression:

\[
θ = (XᵀX)⁻¹Xᵀy
\]

Where:
- \(X\) = Feature matrix (e.g., area, bedrooms, etc.)
- \(y\) = Actual house prices
- \(θ\) = Learned coefficients (weights)

## 🧠 Features

- 📊 Loads CSV data using NumPy
- 🧮 Performs matrix operations for regression
- 📈 Predicts house prices using trained weights
- 💡 Calculates **MAPE (Mean Absolute Percentage Error)**
- 💾 Saves predictions to `predicted_prices.csv`

## 📄 Required Files

- `Housing.csv` – Feature dataset 
- `price.csv` – Target dataset

> ✅ The script automatically skips the first row assuming it's a header.

## 🔧 How to Run

1. Make sure you have Python 3 and NumPy installed:

```bash
pip install numpy
