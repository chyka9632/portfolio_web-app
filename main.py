import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/photo1.jpeg")


with col2:
    st.title("Chika Uchendu")
    with open("profile.txt", "r") as file:
        content = file.read()

    st.info(content)

content1 = """ Check out my recent Python-built apps.
Feel free to reach out!
"""
st.write(content1)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
