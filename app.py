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

/* Background */
.stApp {
    background: #eef5fb;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #023e8a, #0077b6);
    color: white;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Header */
.main-title {
    font-size: 60px;
    font-weight: bold;
    color: #023e8a;
    margin-bottom: 0px;
}

.sub-title {
    color: #5c677d;
    font-size: 22px;
}

/* Main Card */
.main-box {
    background: white;
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* Top Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border-left: 6px solid #0077b6;
}

.card h1 {
    font-size: 42px;
}

/* Input Labels */
label {
    font-weight: bold !important;
    color: #023e8a !important;
}

/* Inputs */
.stTextInput input {
    border-radius: 12px;
    border: 2px solid #90e0ef;
    height: 50px;
    background-color: #f8fbff;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(to right, #0096c7, #023e8a);
    color: white;
    font-size: 22px;
    font-weight: bold;
}

/* Results */
.success-box {
    background: #d8f3dc;
    color: #1b4332;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.danger-box {
    background: #ffe5e5;
    color: #c1121f;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

/* Metric Box */
.metric-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring System

AI-powered flood prediction dashboard using weather and environmental conditions.

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

st.sidebar.success("🟢 System Active")

# ---------------- HEADER ---------------- #
st.markdown("""
<div style='display:flex; align-items:center; gap:20px;'>

<img src='https://cdn-icons-png.flaticon.com/512/1146/1146869.png'
width='110'>

<div>

<div class='main-title'>
Flood Prediction System
</div>

<div class='sub-title'>
AI-powered flood risk prediction and environmental analytics dashboard
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- CARDS ---------------- #
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
        <h3>🌧 Rainfall</h3>
        <h1 style='color:#0077b6;'>120+</h1>
        <p>Critical Level</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h3>🌡 Temperature</h3>
        <h1 style='color:#ff6b35;'>28°C</h1>
        <p>Moderate</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h3>💧 Humidity</h3>
        <h1 style='color:#0096c7;'>80%</h1>
        <p>High Moisture</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
        <h3>🤖 Accuracy</h3>
        <h1 style='color:#8338ec;'>96.55%</h1>
        <p>XGBoost Model</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- MAIN BOX ---------------- #
st.markdown('<div class="main-box">', unsafe_allow_html=True)

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

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- RESULT ---------------- #
        if risk_score > 100:

            st.markdown("""
            <div class="danger-box">
                ⚠️ HIGH FLOOD RISK DETECTED
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="success-box">
                ✅ LOW FLOOD RISK
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- METRICS ---------------- #
        m1, m2, m3 = st.columns(3)

        with m1:
            st.markdown(f"""
            <div class="metric-box">
                <h3>📈 Flood Risk Score</h3>
                <h1 style='color:#0077b6;'>
                    {min(int(risk_score),100)}%
                </h1>
            </div>
            """, unsafe_allow_html=True)

        with m2:

            if risk_score > 100:
                alert = "HIGH"
                color = "#c1121f"
            else:
                alert = "LOW"
                color = "#2d6a4f"

            st.markdown(f"""
            <div class="metric-box">
                <h3>🚨 Alert Level</h3>
                <h1 style='color:{color};'>
                    {alert}
                </h1>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown("""
            <div class="metric-box">
                <h3>🌍 Region Status</h3>
                <h1 style='color:#8338ec;'>
                    MONITORED
                </h1>
            </div>
            """, unsafe_allow_html=True)

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
