import streamlit as st
import joblib
import pandas as pd

model = joblib.load("best_churn_pipeline.pkl")

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score")
age = st.number_input("Age")
balance = st.number_input("Balance")

if st.button("Predict"):
    data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Age": [age],
        "Balance": [balance]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")