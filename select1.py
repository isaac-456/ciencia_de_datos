import streamlit as st
import pandas as pd
st.title("Titanic Dataset")

data = pd.read_cvs("https://raw.githubusercontent.com/adsofito/ciencia-datos/refs/heads/main/titanic.cvs")
st.dataframe(data)
selected_sex = st.selectbox("Select Sex", data['sex'].unique())