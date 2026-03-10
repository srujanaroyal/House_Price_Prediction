import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction")

st.write("Enter house details")

total_area = st.number_input("Total Area")
house_age = st.number_input("House Age")
overall_qual = st.number_input("Overall Quality")

features = np.array([[total_area, house_age, overall_qual]])

if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Estimated Price: ${prediction[0]:,.2f}")