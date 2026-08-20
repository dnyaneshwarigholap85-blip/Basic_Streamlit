import streamlit as st

st.set_page_config(page_title="Dashboard")

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Analytics", "Settings"]
)

if page == "Home":
    st.title("Home Page")
    st.write("Welcome!")

elif page == "Analytics":
    st.title("Analytics Page")
    st.metric("Revenue", "₹50,000")

elif page == "Settings":
    st.title("Settings Page")
    st.write("Configure settings here.")