import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Management")

st.title("Student Management System")

name = st.text_input("Student Name")
age = st.number_input("Age", 1, 100)

if "students" not in st.session_state:
    st.session_state.students = []

if st.button("Add Student"):
    st.session_state.students.append({
        "Name": name,
        "Age": age
    })
    st.success("Student Added")

if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.dataframe(df)