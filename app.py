# ---------------- HEADER ---------------- #
col1, col2 = st.columns([1,5])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4149/4149684.png",
        width=170
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
