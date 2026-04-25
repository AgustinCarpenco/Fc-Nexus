import streamlit as st
import pandas as pd

st.set_page_config(page_title="FC Deportivo Nexus", layout="wide")
col_logo, col_titulo = st.columns([1,5])
with col_logo:
    st.image('nexus_logo.png')
with col_titulo:
   st.title('FC Deportivo Nexus')
   st.markdown('##### Dashboard de Lesiones - Temporada 2024') 

# st.title("FC Deportivo Nexus")
# st.markdown("#### Dashboard de Lesiones · Temporada 2024")
st.divider()

df = pd.read_csv("data/lesiones_nexus.csv")

jugadores = ["Todos"] + sorted(df["jugador"].unique().tolist())
jugador_sel = st.selectbox("Filtrar por jugador", jugadores)

if jugador_sel != "Todos":
    df = df[df["jugador"] == jugador_sel]



st.subheader("Historial de lesiones")
st.dataframe(df, use_container_width=True, hide_index=True)



st.divider()
st.subheader("Lesiones por región corporal")
conteo = df["region"].value_counts()
st.bar_chart(conteo)
st.divider()

