import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import use_case as uc

st.title("Acompanhamento financeiro :blue[cool] :sunglasses:")

options = st.multiselect(
    "Contas",
    ["Itau", "Bradesco", "Inter", "Nubank"]
)

st.write("Conta Selecionada:", options)

map_contas = {'Itau':1,
              'Inter':2,
              'Bradesco':3,
              'Nubank':4}

ids = [map_contas[option] for option in options if option in map_contas]

df_extrato = uc.pesquisar_extrato(ids)

st.dataframe(df_extrato)
