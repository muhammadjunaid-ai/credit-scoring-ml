# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model and mappings
model = joblib.load("model/credit_model.pkl")
mappings = joblib.load("model/mappings.pkl")

st.title("💳 Credit Scoring Prediction App")
st.write("Predict if a customer is a good or bad credit risk.")

# --- User Inputs ---
status_account = st.selectbox(
    "Status Account",
    ["<0 DM", "0 to <200 DM", ">=200 DM / salary", "no checking account"]
)
month_duration = st.number_input("Loan Duration (months)", 1, 72, 12)
credit_history = st.selectbox(
    "Credit History",
    ["good", "poor", "critical", "very good", "no credits"]
)
purpose = st.selectbox(
    "Purpose of Loan",
    ["car", "furniture/equipment", "radio/TV", "education", "business", "others"]
)
credit_amount = st.number_input("Credit Amount", 100, 100000, 5000)
status_savings = st.selectbox(
    "Status Savings",
    ["<100 DM", "100<=X<500 DM", "500<=X<1000 DM", ">=1000 DM", "unknown/ no savings"]
)

# Prepare input DataFrame
input_df = pd.DataFrame({
    "status_account": [status_account],
    "month_duration": [month_duration],
    "credit_history": [credit_history],
    "purpose": [purpose],
    "credit_amount": [credit_amount],
    "status_savings": [status_savings]
})

# Encode categorical columns using saved mappings
for col in ["status_account", "credit_history", "purpose", "status_savings"]:
    input_df[col] = input_df[col].map(mappings[col])
    # If user enters unseen label, default to 0
    input_df[col] = input_df[col].fillna(0)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"✅ Good Credit Risk\nProbability: {probability:.2f}")
    else:
        st.error(f"❌ Bad Credit Risk\nProbability: {probability:.2f}")