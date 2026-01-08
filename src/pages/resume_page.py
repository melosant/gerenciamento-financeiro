import streamlit as st
import pandas as pd
from src.pipelines.filters import filter_entry, filter_output, filter_month, filter_year
from src.pipelines.calculations import difference

st.title('Resumos Financeiros')

df = pd.read_csv('finp.csv')
df = df.set_index(['Data'])

exp_base = st.expander('Base Geral')
tab_geral, tab_entry, tab_out = exp_base.tabs(['Registro Geral', 'Registro de Entradas', 'Registro de Saídas'])

with tab_geral:
    # exibe a base de dados completa
    if len(df) == 0:
        st.warning('Nada registrado na base de dados.')
    else:
        tab_geral.dataframe(df)

with tab_entry:
    # exibe df filtrado por entradas
    filter_entry(df, tab_entry)

with tab_out:
    # exibe df filtrado por saídas
    filter_output(df, tab_out)

exp_resumes = st.expander('Resumos')
tab_mes, tab_ano = exp_resumes.tabs(['Resumo Mês', 'Resumo Ano'])

# exibe df filtrado por mês selecionado e o resumo deste.
df_filtrado_mes = filter_month(df, tab_mes)
col_mes1, col_mes2 = tab_mes.columns(spec=2, border=True)
difference(df_filtrado_mes, tab_mes, col_mes1, col_mes2)

# exibe df filtrado por ano selecionado e o resumo deste.
df_filtrado_ano = filter_year(df, tab_ano)
col_ano1, col_ano2 = tab_ano.columns(spec=2, border=True)
difference(df_filtrado_ano, tab_ano, col_ano1, col_ano2)