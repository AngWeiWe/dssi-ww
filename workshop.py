import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the model
model = joblib.load('model.pkl')

# Title of the app
st.title("E-commerce Customer Repeat Purchase Prediction")

# Function to make predictions
def predict_repeat_purchase(data):
    prediction = model.predict(data)
    return prediction

# Sample input form
st.write("## Enter Customer Details")
age = st.number_input("Age", min_value=18, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
annual_income = st.number_input("Annual Income", min_value=0, value=50000)
purchase_amount = st.number_input("Purchase Amount", min_value=0, value=200)
purchased_category = st.selectbox("Purchased Category", ["Electronics", "Clothing", "HomeGoods", "Books"])
days_since_last_purchase = st.number_input("Days Since Last Purchase", min_value=0, value=10)

# Convert categorical data
gender = 0 if gender == "Male" else 1
categories = {"Electronics": 0, "Clothing": 1, "HomeGoods": 2, "Books": 3}
purchased_category = categories[purchased_category]

# Make prediction
if st.button("Predict Repeat Purchase"):
    input_data = pd.DataFrame([[age, gender, annual_income, purchase_amount, purchased_category, days_since_last_purchase]], 
                              columns=["Age", "Gender", "AnnualIncome", "PurchaseAmount", "PurchasedCategory", "DaysSinceLastPurchase"])
    prediction = predict_repeat_purchase(input_data)
    result = "Yes" if prediction[0] == 1 else "No"
    st.write(f"Repeat Purchase: {result}")

# Dummy data for visualization
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [25, 32, 45, 28, 36, 23, 50, 29, 40, 34],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "AnnualIncome": [50000, 60000, 80000, 45000, 75000, 30000, 100000, 52000, 90000, 65000],
    "PurchaseAmount": [200, 150, 300, 50, 250, 100, 400, 70, 350, 180],
    "PurchasedCategory": ["Electronics", "Clothing", "HomeGoods", "Books", "Electronics", "Clothing", "HomeGoods", "Books", "Electronics", "Clothing"],
    "DaysSinceLastPurchase": [10, 20, 5, 15, 2, 30, 1, 25, 8, 12],
    "RepeatPurchase": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
}

# Convert dummy data to DataFrame
df = pd.DataFrame(data)

# Visualize data
st.write("## Purchase Distribution by Category")
category_counts = df['PurchasedCategory'].value_counts()

fig, ax = plt.subplots()
category_counts.plot(kind='bar', ax=ax)
ax.set_title("Number of Purchases by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Number of Purchases")

# Display the chart
st.pyplot(fig)

