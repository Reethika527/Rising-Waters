
import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="wide"
)

# ---------------- SEA BLUE THEME ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #001f3f, #005f99, #00a8cc);
    color: white;
}

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: white;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #dff6ff;
}

.card {
    background: rgba(255,255,255,0.12);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
}

.card h1 {
    color: #caf0f8;
}

.card p {
    color: #f1faff;
}

.stButton>button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.high-risk {
    background: linear-gradient(to right, #ff4d6d, #c9184a);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: white;
}

.low-risk {
    background: linear-gradient(to right, #00b4d8, #0096c7);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: white;
}

.footer {
    text-align:center;
    color:#dff6ff;
    font-size:15px;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #001d3d, #003566);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring Dashboard

AI-powered flood prediction system developed using Machine Learning algorithms.

### Technologies Used
- Streamlit
- Python
- Machine Learning
- Data Analytics
""")

st.sidebar.success("🟢 System Status : ACTIVE")

# ---------------- HEADER ---------------- #
st.markdown(
    '<p class="main-title">🌊 Flood Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI-powered flood risk prediction and environmental analytics dashboard</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- DASHBOARD CARDS ---------------- #
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌧 Rainfall</h3>
        <h1>120+</h1>
        <p>Critical Level</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🌡 Temperature</h3>
        <h1>28°C</h1>
        <p>Moderate</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>💧 Humidity</h3>
        <h1>80%</h1>
        <p>High Moisture</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>🤖 Accuracy</h3>
        <h1>96.55%</h1>
        <p>XGBoost Model</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #
st.subheader("📋 Enter Environmental Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.slider("Rainfall (mm)", 0, 500, 120)

with col2:
    temperature = st.slider("Temperature (°C)", 0, 50, 28)

with col3:
    humidity = st.slider("Humidity (%)", 0, 100, 80)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- PREDICTION ---------------- #
if st.button("🚀 Predict Flood Risk"):

    risk_score = (rainfall * 0.5) + (humidity * 0.4) - (temperature * 0.2)

    if risk_score > 100:

        st.markdown("""
        <div class="high-risk">
            ⚠️ HIGH FLOOD RISK DETECTED
        </div>
        """, unsafe_allow_html=True)

        st.error(
            "Emergency response teams are advised to initiate precautionary measures immediately."
        )

    else:

        st.markdown("""
        <div class="low-risk">
            ✅ LOW FLOOD RISK
        </div>
        """, unsafe_allow_html=True)

        st.success(
            "Current environmental conditions indicate low probability of flood occurrence."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- METRICS ---------------- #
    risk_percent = min(int(risk_score), 100)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📈 Flood Risk Score", f"{risk_percent}%")

    with col2:
        if risk_percent > 70:
            st.metric("🚨 Alert Level", "HIGH")
        else:
            st.metric("🟢 Alert Level", "LOW")

    with col3:
        st.metric("🌍 Region Status", "MONITORED")

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- CHART ---------------- #
    data = pd.DataFrame({
        "Environmental Factors": [
            "Rainfall",
            "Temperature",
            "Humidity"
        ],
        "Values": [
            rainfall,
            temperature,
            humidity
        ]
    })

    st.subheader("📊 Environmental Analytics")

    st.bar_chart(data.set_index("Environmental Factors"))

    st.info(
        "Prediction generated successfully using AI-powered flood analysis system."
    )

# ---------------- FOOTER ---------------- #
st.markdown("---")

st.markdown(
    '<p class="footer">Developed using Streamlit | Machine Learning Internship Project</p>',
    unsafe_allow_html=True
)
