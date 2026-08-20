import streamlit as st

st.title("File Upload")

uploaded_file = st.file_uploader(
    "Upload a file"
)

if uploaded_file:
    st.success("File Uploaded Successfully")
    st.write("Filename:", uploaded_file.name)