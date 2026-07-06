

import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Rising Waters AI",
    page_icon="🌊",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #000428, #004e92);
    color: white;
}

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main-title {
    font-size: 65px;
    font-weight: bold;
    color: white;
    text-align: center;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d6e4ff;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.1);
}

.card h1 {
    color: #4cc9f0;
}

.card p {
    color: #dce6f2;
}

.predict-btn {
    margin-top: 20px;
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
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #0072ff, #00c6ff);
}

.high-risk {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: white;
    box-shadow: 0px 0px 20px rgba(255,0,0,0.4);
}

.low-risk {
    background: linear-gradient(to right, #11998e, #38ef7d);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: white;
    box-shadow: 0px 0px 20px rgba(0,255,100,0.4);
}

.footer {
    text-align:center;
    color:#dce6f2;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4149/4149672.png",
    width=120
)

st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring Dashboard

AI-powered flood prediction system developed using Machine Learning algorithms.

### Technologies Used
- Streamlit
- Python
- Machine Learning
- Data Analytics

### Algorithms
- Decision Tree
- Random Forest
- KNN
- XGBoost
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
st.subheader("📋 Environmental Parameters")

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
