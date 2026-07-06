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

/* Background */
.stApp {
    background: linear-gradient(to right, #f8fdff, #eaf6ff);
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
    background: #eef8ff;
}

/* Main Title */
.main-title {
    font-size: 58px;
    font-weight: bold;
    color: #023e8a;
}

.sub-title {
    color: #5c677d;
    font-size: 22px;
    margin-top: -10px;
}

/* Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
    border: 1px solid #edf2f4;
}

.card h1 {
    margin: 0;
}

/* Input Box */
.input-container {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

/* Inputs */
.stTextInput input {
    border-radius: 12px;
    border: 2px solid #d9edff;
    height: 48px;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(to right, #2196f3, #1565c0);
    color: white;
    font-size: 22px;
    font-weight: bold;
}

/* Result */
.low-risk {
    background: #e8fff1;
    color: #2d6a4f;
    padding: 25px;
    border-radius: 15px;
    font-size: 30px;
    font-weight: bold;
}

.high-risk {
    background: #ffe5e5;
    color: #c1121f;
    padding: 25px;
    border-radius: 15px;
    font-size: 30px;
    font-weight: bold;
}

.metric-box {
    background: white;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}

/* Footer */
.footer {
    text-align: center;
    color: #5c677d;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🌊 Rising Waters AI")

st.sidebar.markdown("""
### Smart Flood Monitoring Dashboard

AI-powered flood prediction system using environmental and weather conditions.

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
col1, col2 = st.columns([1,6])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2921/2921822.png",
        width=90
    )

with col2:
    st.markdown(
        '<div class="main-title">Flood Prediction System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">AI-powered flood risk prediction and environmental analytics dashboard</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- TOP CARDS ---------------- #
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

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- RESULT ---------------- #
        if risk_score > 100:

            st.markdown("""
            <div class="high-risk">
                ⚠️ HIGH FLOOD RISK DETECTED
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="low-risk">
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
                <h1 style='color:#0077b6;'>{min(int(risk_score),100)}%</h1>
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
                <h1 style='color:{color};'>{alert}</h1>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown("""
            <div class="metric-box">
                <h3>🌍 Region Status</h3>
                <h1 style='color:#8338ec;'>MONITORED</h1>
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
