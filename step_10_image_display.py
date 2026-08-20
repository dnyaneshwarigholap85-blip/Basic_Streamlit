import streamlit as st

st.title("Image Viewer")

image = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if image:
    st.image(image)