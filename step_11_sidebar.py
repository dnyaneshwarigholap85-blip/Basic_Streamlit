import streamlit as st

st.title("Sidebar Example")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "About", "Contact"]
)

st.write("Current Page:", page)