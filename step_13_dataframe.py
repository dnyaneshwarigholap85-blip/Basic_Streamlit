import streamlit as st
import pandas as pd

st.title("DataFrame Example")

data = {
    "Name": ["Rahul", "Amit", "Neha"],
    "Age": [25, 30, 22]
}

df = pd.DataFrame(data)

st.dataframe(df)