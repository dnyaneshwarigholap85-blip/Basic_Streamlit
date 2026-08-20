import streamlit as st

st.title("Selectbox Example")

city = st.selectbox(
    "Choose your city",
    ["Mumbai", "Pune", "Nashik", "Delhi"]
)

st.write("Selected City:", city)