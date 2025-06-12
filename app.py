import streamlit as st
import joblib
import pandas as pd

st.title("Calculate Your House Price Here!!!")
model = joblib.load('house_price_model.pkl')
features = joblib.load('features.pkl')  

YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
TotalBsmtSF = st.number_input("Total Basement SF", min_value=0, value=1000)
LotArea = st.number_input("Lot Area", min_value=1000, value=5000)
MSSubClass = st.number_input("MS SubClass", min_value=1, value=20)
YearRemodAdd = st.number_input("Year Remodeled", min_value=1900, max_value=2025, value=2005)

if st.button("Predict Price"):
   
    input_dict = {
        'YearBuilt': YearBuilt,
        'TotalBsmtSF': TotalBsmtSF,
        'LotArea': LotArea,
        'MSSubClass': MSSubClass,
        'YearRemodAdd': YearRemodAdd
    }
    input_df = pd.DataFrame([input_dict])[features]  

    predicted_price = model.predict(input_df)[0]
    st.success(f"Predicted House Price: ₹{predicted_price:,.0f}")
