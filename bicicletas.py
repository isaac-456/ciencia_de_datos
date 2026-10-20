import streamlit as st
import pandas as pd
st.title("Uso de Bicicletas")

data =pd.read_csv("https://raw.githubusercontent.com/adsoftsito/nosql/refs/heads/main/csv/citibike-tripdata.csv")
st.dataframe(data)

with st.sidebar:
    st.header("Buscador")
    texto_busqueda = st.text_input("Buscar película por título:")

if texto_busqueda:
    filtered_data = data[data['name'].str.contains(texto_busqueda, case=False, na=False)]
    st.write(f"Resultados para: *{texto_busqueda}*")
    st.dataframe(filtered_data)
else:
    st.dataframe(data)

selected_director = st.selectbox("Select Director", data['director'].unique())
filtered_data_director = data[data['director']==selected_director]

st.dataframe(filtered_data_director)
st.write("Realizado por:")
st.write("Emilianoi Rico Borbonio")
st.write("Isaac Becerril Carrera")