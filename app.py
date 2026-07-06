import streamlit as st

st.title("Flood Prediction System")

rainfall = st.number_input("Enter Rainfall (mm)")

temperature = st.number_input("Enter Temperature")

humidity = st.number_input("Enter Humidity")

if st.button("Predict Flood"):

    if rainfall > 100 and humidity > 70:
        st.error("High Chance of Flood")
    else:
        st.success("Low Chance of Flood")
