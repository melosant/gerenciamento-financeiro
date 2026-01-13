import streamlit as st
import pandas as pd
from src.utils.filters import filter_month, filter_year
from src.utils.calculations import difference

df = pd.read_csv('finp.csv')
df = df.set_index(['Data'])

st.title('Resumos FINP')

tab_mes, tab_ano = st.tabs(['Resumo Mês', 'Resumo Ano'])

# exibe df filtrado por mês selecionado e o resumo deste.
df_filtrado_mes = filter_month(df, tab_mes)
col_mes1, col_mes2 = tab_mes.columns(spec=2, border=True)
col_mes3, col_mes4 = tab_mes.columns(spec=2, border=True)
difference(df_filtrado_mes, tab_mes, col_mes1, col_mes2, col_mes3, col_mes4)

# exibe df filtrado por ano selecionado e o resumo deste.
df_filtrado_ano = filter_year(df, tab_ano)
col_ano1, col_ano2 = tab_ano.columns(spec=2, border=True)
col_ano3, col_ano4 = tab_ano.columns(spec=2, border=True)
difference(df_filtrado_ano, tab_ano, col_ano1, col_ano2, col_ano3, col_ano4)