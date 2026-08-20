import streamlit as st

st.title("Slider Example")

age = st.slider(
    "Select Age",
    1,
    100,
    25
)

st.write("Age:", age)