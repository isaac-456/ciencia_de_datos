import streamlit as st
import pandas as st
name_link = "https://raw.githubusercontent.com/adsofito/ciencia-datos"
names_data=pd.read_csv(names link)

st.title("streamlit and pandas")
st.dataframe(names_data)