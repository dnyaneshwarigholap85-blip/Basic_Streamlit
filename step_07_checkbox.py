import streamlit as st

st.title("Checkbox Example")

python = st.checkbox("Python")
java = st.checkbox("Java")
sql = st.checkbox("SQL")

skills = []

if python:
    skills.append("Python")

if java:
    skills.append("Java")

if sql:
    skills.append("SQL")

st.write("Skills:", skills)