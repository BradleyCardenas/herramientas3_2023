import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()
st.dataframe(df)

listaPaises = df['country'].unique()

# Creando el sidebar
with st.sidebar:
    pais = st.selectbox('Paises', listaPaises)
    st.write(pais)

# El body
datosPais = df.query("country == '"+ pais + "'")
fig = px.bar(datosPais, x = 'year', y = 'pop')
st.plotly_chart(fig, use_container_width = True)
