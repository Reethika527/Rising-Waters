import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Flood Prediction System",
    page_icon="🌊",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background-color:#f4f8fc;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.main-title{
    text-align:center;
    font-size:58px;
    font-weight:bold;
    color:#023e8a;
}

.sub-title{
    text-align:center;
    color:#5c677d;
    font-size:22px;
    margin-bottom:30px;
}

/* Containers */
.block{
    background:white;
    padding:30px;
    border-radius:18px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:#0077b6;
    color:white;
    font-size:22px;
    font-weight:bold;
}

/* Success */
.success-box{
    background:#d8f3dc;
    color:#1b4332;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

/* Danger */
.danger-box{
    background:#ffe5e5;
    color:#c1121f;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("""
<div class='main-title'>
🌊 Flood Prediction System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
AI-powered flood risk prediction dashboard
</div>
""", unsafe_allow_html=True)

# ---------------- TWO COLUMNS ---------------- #
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
        august
    )

    if score > 4500:

        st.markdown("""
        <div class='danger-box'>
        ⚠️ HIGH FLOOD RISK DETECTED
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class='success-box'>
        ✅ LOW FLOOD RISK
        </div>
        """, unsafe_allow_html=True)
