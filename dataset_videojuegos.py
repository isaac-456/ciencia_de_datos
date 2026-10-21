import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Videojuegos Dataset")

data = pd.read_csv("https://gist.githubusercontent.com/designernatan/27da044c6dc823f7ac7fe3a01f4513ed/raw/d15b5c7d7a5efb38750b16ec935fc126ec9a6e79/vgsales.csv")

with st.sidebar:
    juegos = st.checkbox("Mostrar todos los juegos")
    texto_busqueda = st.text_input("Buscar por título:")
    grafica1 = st.checkbox("Grafica 1")
    grafica2 = st.checkbox("Grafica 2")
    grafica3 = st.checkbox("Grafica 3")
    
    st.markdown("---")
    filtro_slider = st.slider("Slider (Grafica 1)", int(data['Year'].min()), int(data['Year'].max()), (int(data['Year'].min()), int(data['Year'].max())))
    filtro_radio = st.radio("Radio (Grafica 2)", ["Global", "Norteamérica"])
    filtro_lista = st.selectbox("Lista (Grafica 3)", data['Genre'].dropna().unique())

if juegos:
    st.write(f"Todos los Videojuegos")
    st.dataframe(data)

if texto_busqueda:
    filtered_data = data[data['Name'].str.contains(texto_busqueda, case=False, na=False)]
    st.write(f"Resultados para: {texto_busqueda}")
    st.dataframe(filtered_data)

if grafica1:
    st.header("Lanzamientos por año")
    fig, ax = plt.subplots()
    data_g1 = data[(data['Year'] >= filtro_slider[0]) & (data['Year'] <= filtro_slider[1])]
    ax.hist(data_g1['Year'].dropna(), bins=20)
    st.pyplot(fig)

if grafica2:
    fig2, ax2 = plt.subplots()
    if filtro_radio == "Global":
        ventas_totales = data.groupby('Genre')['Global_Sales'].sum()
    else:
        ventas_totales = data.groupby('Genre')['NA_Sales'].sum()
    ax2.barh(ventas_totales.index, ventas_totales.values)
    ax2.set_ylabel("Género")
    ax2.set_xlabel("Ventas (Millones)")
    ax2.set_title("Ventas de Videojuegos por Género")
    st.header("Grafica de Barras de Videojuegos")
    st.pyplot(fig2)

if grafica3:
    st.header("Titulos por Plataforma")
    fig3, ax3 = plt.subplots()
    data_g3 = data[data['Genre'] == filtro_lista]
    platform_data = data_g3['Platform'].value_counts().head(6)
    ax3.pie(platform_data, labels=platform_data.index, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    st.pyplot(fig3)

if st.sidebar.button("Sobre mi"):
        st.write("Nombre: Isaac Becerril Carrera")
        st.write("Matricula: zS26004583")
        map_data = pd.DataFrame({
          'lat':[18.8375], 'lon':[-97.1375]   
        })
        st.subheader(f"Ciudad Natal")
        st.map(map_data,zoom=14)

        



