
import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background-color: #f4fbff;
}

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    color: #003566;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #dff6ff, #caf0f8);
}

/* Header */

.main-title {
    font-size: 60px;
    font-weight: bold;
    color: #023e8a;
    text-align: center;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #0077b6;
}

/* Cards */

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border: 2px solid #dff6ff;
}

.card h1 {
    color: #0077b6;
}

.card p {
    color: #555;
}

/* Input Boxes */

.stNumberInput input {
    background-color: white !important;
    border-radius: 10px !important;
    border: 2px solid #90e0ef !important;
    height: 45px;
}

/* Button */

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(to right, #00b4d8, #0077b6);
    color: white;
    font-size: 22px;
    font-weight: bold;
}

/* Result */

.high-risk {
    background: #ffccd5;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #c1121f;
}

.low-risk {
    background: #d8f3dc;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #2d6a4f;
}

/* Footer */

.footer {
    text-align:center;
    color:#0077b6;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring System

AI-powered flood prediction dashboard using environmental parameters.

### Features
✅ Real-time Prediction  
✅ Risk Analysis  
✅ Environmental Monitoring  
✅ AI-Based System  
""")

st.sidebar.success("🟢 System Active")

# ---------------- HEADER ---------------- #
st.markdown(
    '<p class="main-title">Flood Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI-powered flood risk prediction and environmental monitoring dashboard</p>',
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
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0,
        max_value=500,
        value=120
    )

with col2:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0,
        max_value=50,
        value=28
    )

with col3:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0,
        max_value=100,
        value=80
    )

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
            "Emergency response teams should take precautionary measures immediately."
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

    st.subheader("📊 Environmental Analysis")

    st.bar_chart(data.set_index("Environmental Factors"))

# ---------------- FOOTER ---------------- #
st.markdown("---")

st.markdown(
    '<p class="footer">Developed using Streamlit | Machine Learning Internship Project</p>',
    unsafe_allow_html=True
)
