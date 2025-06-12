# 🏡 House Price Prediction App  Link - https://housepricepredictior.streamlit.app

This is a machine learning project that predicts the sale price of houses based on various input features such as
area, year built, condition, and more. It includes a trained model and a Streamlit web app where users can input house details and get a predicted price.

---

## 📁 Project Structure

house-price-predictor/
├── data/
│ └── HousePricePrediction.xlsx
├── models/
│ └── house_price_model.pkl
├── app.py
├── requirements.txt
└── README.md

---

## 🔑 Features Used

- `YearBuilt`
- `TotalBsmtSF`
- `LotArea`
- `MSSubClass`
- `OverallCond`
- Plus encoded categorical features like `Exterior1st`, `LotConfig`, etc.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor

pip install -r requirements.txt
streamlit run app.py
⚙️ Model Info
Model: RandomForestRegressor

Metrics:
MSE: Mean Squared Error
R² Score: Goodness of fit

Processing:
Handled missing values
One-hot encoding for categorical columns
Train/test split (80/20)


