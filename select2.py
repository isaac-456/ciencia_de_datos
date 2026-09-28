import streamlit as st
import pandas as pd
st.title("Titanic Dataset")

data =pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_embarked = st.selectbox("Select Embarked", data['embarked'].unique())
filtered_data_embarked = data[data['embarked']==selected_embarked]

st.dataframe(filtered_data_embarked)