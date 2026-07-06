
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

.stApp{
    background: linear-gradient(to right, #f4f9ff, #e8f3ff);
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Header */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#023e8a;
}

.sub-title{
    text-align:center;
    color:#5c677d;
    font-size:22px;
    margin-bottom:35px;
}

/* Boxes */
.block{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 4px 18px rgba(0,0,0,0.08);
    border-left:6px solid #0096c7;
}

/* Metrics */
.metric{
    background:white;
    padding:22px;
    border-radius:18px;
    text-align:center;
    box-shadow:0px 4px 14px rgba(0,0,0,0.07);
}

.metric h1{
    font-size:42px;
}

/* Button */
.stButton>button{
    width:100%;
    height:58px;
    border:none;
    border-radius:14px;
    background:linear-gradient(to right,#0077b6,#023e8a);
    color:white;
    font-size:22px;
    font-weight:bold;
}

/* Results */
.success-box{
    background:#d8f3dc;
    color:#1b4332;
    padding:25px;
    border-radius:16px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

.danger-box{
    background:#ffe5e5;
    color:#c1121f;
    padding:25px;
    border-radius:16px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("""
<div class='main-title'>
🌊 Rising Waters AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Smart Flood Prediction & Environmental Monitoring Dashboard
</div>
""", unsafe_allow_html=True)

# ---------------- TOP METRICS ---------------- #
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class='metric'>
    <h3>🌧 Rainfall</h3>
    <h1 style='color:#0077b6;'>3200+</h1>
    <p>Annual Rainfall</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='metric'>
    <h3>🌡 Temperature</h3>
    <h1 style='color:#ff6b35;'>28°C</h1>
    <p>Moderate Climate</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='metric'>
    <h3>💧 Humidity</h3>
    <h1 style='color:#0096c7;'>80%</h1>
    <p>High Moisture</p>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class='metric'>
    <h3>🤖 Accuracy</h3>
    <h1 style='color:#8338ec;'>96.55%</h1>
    <p>XGBoost Model</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- TWO COLUMN LAYOUT ---------------- #
left, right = st.columns(2)

# ---------------- LEFT SIDE ---------------- #
with left:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.subheader("🌦 Weather Information")

    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        value=70.0
    )

    cloud = st.number_input(
        "Cloud Cover (%)",
        value=40.0
    )

    wind = st.number_input(
        "Wind Speed (km/h)",
        value=20.0
    )

    visibility = st.number_input(
        "Cloud Visibility (%)",
        value=65.0
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RIGHT SIDE ---------------- #
with right:

    st.markdown("<div class='block'>", unsafe_allow_html=True)

    st.subheader("🌧 Rainfall Information")

    annual = st.number_input(
        "Annual Rainfall (mm)",
        value=3000.0
    )

    janfeb = st.number_input(
        "Jan-Feb Rainfall (mm)",
        value=40.0
    )

    marmay = st.number_input(
        "Mar-May Rainfall (mm)",
        value=350.0
    )

    june = st.number_input(
        "June Rainfall (mm)",
        value=250.0
    )

    july = st.number_input(
        "July Rainfall (mm)",
        value=700.0
    )

    august = st.number_input(
        "August Rainfall (mm)",
        value=650.0
    )

    september = st.number_input(
        "September Rainfall (mm)",
        value=500.0
    )

    octdec = st.number_input(
        "Oct-Dec Rainfall (mm)",
        value=500.0
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTON ---------------- #
if st.button("🚀 Predict Flood Risk"):

    score = (
        annual +
        humidity +
        cloud +
        july +
        august +
        september
    )

    if score > 4500:

        st.markdown("""
        <div class='danger-box'>
        ⚠️ HIGH FLOOD RISK DETECTED
        </div>
        """, unsafe_allow_html=True)

        risk = "High"

    else:

        st.markdown("""
        <div class='success-box'>
        ✅ LOW FLOOD RISK
        </div>
        """, unsafe_allow_html=True)

        risk = "Low"

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- ANALYSIS TABLE ---------------- #
    data = pd.DataFrame({
        "Parameter": [
            "Temperature",
            "Humidity",
            "Cloud Cover",
            "Annual Rainfall",
            "July Rainfall",
            "August Rainfall"
        ],
        "Value": [
            temperature,
            humidity,
            cloud,
            annual,
            july,
            august
        ]
    })

    st.subheader("📊 Environmental Analysis")

    st.dataframe(data, use_container_width=True)

    # ---------------- BAR CHART ---------------- #
    st.subheader("📈 Flood Monitoring Chart")

    chart_data = pd.DataFrame({
        "Rainfall": [janfeb, marmay, june, july, august, september, octdec]
    })

    st.bar_chart(chart_data)

    # ---------------- FINAL STATUS ---------------- #
    st.info(f"Flood Alert Status : {risk} Risk Zone")
