import streamlit as st
import pandas as pd
st.title("Peliculas Dataset")

data =pd.read_csv("https://raw.githubusercontent.com/RyuoX1/ciencia-de-datos/refs/heads/main/movies.csv")

with st.sidebar:
    st.header("Buscador")
    texto_busqueda = st.text_input("Buscar película por título:")
    boton_buscar = st.button("Buscar por titulo")

    selected_director = st.selectbox("Select Director", data['director'].unique())
    filtered_data_director = data[data['director']==selected_director]
    boton_buscar_director = st.button("Filtrar por director")

if boton_buscar and texto_busqueda:
    filtered_data = data[data['name'].str.contains(texto_busqueda, case=False, na=False)]
    st.write(f"Resultados para: *{texto_busqueda}*")
    st.dataframe(filtered_data)

if boton_buscar_director:
    filtered_data_director = data[data['director'] == selected_director]
    st.header(f"Películas dirigidas por: {selected_director}")
    st.dataframe(filtered_data_director)
