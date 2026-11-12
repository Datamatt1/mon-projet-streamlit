import streamlit as st
import pandas as pd

taxis=pd.read_csv("taxis.csv")

st.title(" Dashboard Analyse Taxis - Matthieu ")


choix_quartier = st.selectbox(
 "Choisissez votre quartier de prise en charge :",
 taxis["pickup_borough"].unique().dropna()
)

st.dataframe(taxis[taxis["pickup_borough"] == choix_quartier].head(5))
st.metric(label = "Nombre de courses dans cet arrondissement", value=len(taxis[taxis["pickup_borough"]==choix_quartier]))