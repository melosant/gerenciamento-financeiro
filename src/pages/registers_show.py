import streamlit as st
import pandas as pd
from src.utils.filters import filter_entry, filter_output
st.title('Resumos Financeiros')

df = pd.read_csv('finp.csv')
df = df.set_index(['Data'])

tab_geral, tab_entry, tab_out = st.tabs(['Registro Geral', 'Registro de Entradas', 'Registro de Saídas'])

with tab_geral:
    # exibe a base de dados completa
    if len(df) == 0:
        tab_geral.warning('Nada registrado na base de dados.')
    else:
        # um df novo recebe uma cópia para formatar a coluna valor
        df_format = df.copy()
        df_format['Valor'] = df_format['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))
        tab_geral.dataframe(df_format)

with tab_entry:
    # exibe df filtrado por entradas
    filter_entry(df, tab_entry)

with tab_out:
    # exibe df filtrado por saídas
    filter_output(df, tab_out)