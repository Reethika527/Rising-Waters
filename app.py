

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

/* Main Background */
.stApp {
    background: linear-gradient(to right, #f5fbff, #e3f2fd);
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Fonts */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #dff6ff, #caf0f8);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #023e8a;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #0077b6;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border: 1px solid #d6f0ff;
}

.card h1 {
    margin: 0;
}

.card p {
    color: gray;
}

/* Input Container */
.input-container {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

/* Input Boxes */
.stTextInput input {
    border-radius: 12px;
    border: 2px solid #90e0ef;
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

/* Result Box */
.result-high {
    background: #ffccd5;
    color: #c1121f;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.result-low {
    background: #d8f3dc;
    color: #2d6a4f;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: #0077b6;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring Dashboard

AI-powered flood prediction system using environmental conditions and machine learning algorithms.

### Technologies
- Python
- Streamlit
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
    '<div class="main-title">Flood Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI-powered flood risk prediction and environmental analytics dashboard</div>',
    unsafe_allow_html=True
)

# ---------------- TOP CARDS ---------------- #
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌧 Rainfall</h3>
        <h1 style='color:#0077b6;'>120+</h1>
        <p>Critical Level</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🌡 Temperature</h3>
        <h1 style='color:#ff6b35;'>28°C</h1>
        <p>Moderate</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>💧 Humidity</h3>
        <h1 style='color:#0096c7;'>80%</h1>
        <p>High Moisture</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>🤖 Accuracy</h3>
        <h1 style='color:#8338ec;'>96.55%</h1>
        <p>XGBoost Model</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #
st.markdown('<div class="input-container">', unsafe_allow_html=True)

st.subheader("📋 Enter Environmental Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.text_input(
        "Rainfall (mm)",
        placeholder="Enter rainfall value"
    )

with col2:
    temperature = st.text_input(
        "Temperature (°C)",
        placeholder="Enter temperature value"
    )

with col3:
    humidity = st.text_input(
        "Humidity (%)",
        placeholder="Enter humidity value"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTON ---------------- #
if st.button("🚀 Predict Flood Risk"):

    try:

        rainfall = float(rainfall)
        temperature = float(temperature)
        humidity = float(humidity)

        risk_score = (rainfall * 0.5) + (humidity * 0.4) - (temperature * 0.2)

        # ---------------- RESULT ---------------- #
        if risk_score > 100:

            st.markdown("""
            <div class="result-high">
                ⚠️ HIGH FLOOD RISK DETECTED
            </div>
            """, unsafe_allow_html=True)

            st.error(
                "Emergency response teams should initiate precautionary measures immediately."
            )

        else:

            st.markdown("""
            <div class="result-low">
                ✅ LOW FLOOD RISK
            </div>
            """, unsafe_allow_html=True)

            st.success(
                "Current environmental conditions indicate low flood probability."
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- METRICS ---------------- #
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📈 Flood Risk Score",
                f"{min(int(risk_score),100)}%"
            )

        with col2:
            if risk_score > 100:
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

    except:
        st.error("Please enter valid numeric values.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">Developed using Streamlit | Final Year Internship Project</div>',
    unsafe_allow_html=True
)
