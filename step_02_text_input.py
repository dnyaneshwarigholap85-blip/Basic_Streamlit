import streamlit as st

st.title("User Input Example")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")