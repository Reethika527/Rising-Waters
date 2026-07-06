

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #001f3f, #0077b6, #00b4d8);
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
    color: #dff6ff;
}

.card {
    background: rgba(255,255,255,0.12);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.15);
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
    background: linear-gradient(to right, #00b4d8, #0077b6);
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
