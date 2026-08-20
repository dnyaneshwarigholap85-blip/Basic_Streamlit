import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

if st.button("Add"):
    st.write("Result:", num1 + num2)