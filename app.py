import streamlit as st

st.set_page_config(page_title="Flood Prediction", page_icon="🌊")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    h1 {
        color: #0066cc;
        text-align: center;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌊 Flood Prediction System")

st.write("Enter weather details to predict flood chances.")

rainfall = st.slider("Rainfall (mm)", 0, 500, 50)
temperature = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 60)

if st.button("Predict Flood"):

    if rainfall > 120 and humidity > 70:
        st.error("⚠️ High Chance of Flood")
    else:
        st.success("✅ Low Chance of Flood")

st.markdown("---")
st.caption("Developed using Streamlit")
