import streamlit as st

st.title("Button Example")

if st.button("Click Me"):
    st.success("Button Clicked!")