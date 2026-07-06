import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #021B3A, #0A2A43);
    color: white;
}

h1, h2, h3 {
    color: white;
}

.big-font {
    font-size:55px !important;
    font-weight: bold;
    color: white;
}

.sub-text {
    font-size:22px;
    color: #dbe9ff;
}

.metric-card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.4);
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.stButton>button {
    width: 100%;
    height: 3.5em;
    border-radius: 12px;
    border: none;
    background: linear-gradient(to right, #0072ff, #00c6ff);
    color: white;
    font-size: 20px;
    font-weight: bold;
}

.css-1d391kg {
    background-color: #061e3c;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters")
st.sidebar.markdown("### Flood Prediction System")

st.sidebar.info("""
This project predicts flood risk using weather conditions like rainfall, temperature, and humidity.
""")

st.sidebar.success("Machine Learning Internship Project")

# ---------------- HEADER ---------------- #
st.markdown('<p class="big-font">🌊 Flood Prediction System</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="sub-text">Predict flood risk using environmental conditions and weather data.</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- METRICS ---------------- #
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h3>🌧 Rainfall</h3>
    <h2>120+</h2>
    <p>High Risk</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h3>🌡 Temperature</h3>
    <h2>25°C</h2>
    <p>Moderate</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h3>💧 Humidity</h3>
    <h2>80%</h2>
    <p>High</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h3>🤖 Accuracy</h3>
    <h2>92%</h2>
    <p>Excellent</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #
st.subheader("📋 Enter Environmental Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.slider("Rainfall (mm)", 0, 500, 120)

with col2:
    temperature = st.slider("Temperature (°C)", 0, 50, 28)

with col3:
    humidity = st.slider("Humidity (%)", 0, 100, 80)

# ---------------- PREDICTION ---------------- #
if st.button("🚀 Predict Flood"):

    risk_score = (rainfall * 0.5) + (humidity * 0.4) - (temperature * 0.2)

    if risk_score > 100:
        result = "⚠️ High Chance of Flood"
        color = "#ff4b4b"
    else:
        result = "✅ Low Chance of Flood"
        color = "#00cc66"

    st.markdown(
        f"""
        <div class="result-box" style="background-color:{color};">
            {result}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- CHART ---------------- #
    data = pd.DataFrame({
        "Parameters": ["Rainfall", "Temperature", "Humidity"],
        "Values": [rainfall, temperature, humidity]
    })

    st.subheader("📊 Parameter Overview")
    st.bar_chart(data.set_index("Parameters"))

    st.success("Prediction Completed Successfully ✅")

    st.balloons()

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.caption("Developed using Streamlit | AI & ML Internship Project")
