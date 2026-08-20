import streamlit as st

st.title("Radio Example")

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

st.write("Selected:", gender)