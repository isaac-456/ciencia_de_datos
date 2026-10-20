import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Videojuegos Dataset")

data =pd.read_csv("https://gist.githubusercontent.com/designernatan/27da044c6dc823f7ac7fe3a01f4513ed/raw/d15b5c7d7a5efb38750b16ec935fc126ec9a6e79/vgsales.csv")

with st.sidebar:
    juegos = st.checkbox("Mostrar todos los juegos")
    texto_busqueda = st.text_input("Buscar por título:")
    grafica1 = st.checkbox("Grafica 1")
    grafica2 = st.checkbox("Grafica 2")
    grafica3 = st.checkbox("Grafica 3")

if juegos:
    st.write(f"Todos los Videojuegos")
    st.dataframe(data)

if texto_busqueda:
    filtered_data = data[data['Name'].str.contains(texto_busqueda, case=False, na=False)]
    st.write(f"Resultados para: *{texto_busqueda}*")
    st.dataframe(filtered_data)

if grafica1: 
    st.header("Lanzamientos por año")
    fig, ax = plt.subplots()
    ax.hist(data['Year'].dropna(), bins=20)
    st.pyplot(fig)

if grafica2: 
    fig2, ax2 = plt.subplots()
    ventas_totales = data.groupby('Genre')['Global_Sales'].sum()
    
    ax2.barh(ventas_totales.index, ventas_totales.values)
    ax2.set_ylabel("Género")
    ax2.set_xlabel("Ventas Globales (Millones)")
    ax2.set_title("Ventas de Videojuegos por Género")
    
    st.header("Grafica de Barras de Videojuegos")
    st.pyplot(fig2)

if grafica3:
    st.header("Titulos por Plataforma")
    fig3, ax3 = plt.subplots()
    platform_data = data['Platform'].value_counts().head(6)
    ax3.pie(platform_data, labels=platform_data.index, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)

if st.button("Sobre mi"):
    def mostrar_creador():
        st.write("Nombre: Isaac Becerril Carrera")
        st.write("Matricula: zS26004583")
        



