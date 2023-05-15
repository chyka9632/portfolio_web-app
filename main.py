import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Chika Uchendu")
    with open("profile.txt", "r") as file:
        content = file.read()

    st.write(content)