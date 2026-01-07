import streamlit as st
import pandas as pd
from src.func_df_streamlit import register_entry, register_output, filter_entry, filter_output

st.title('Gestão Financeira')
st.markdown('''_Pressione "R" para atualizar a página e as tabelas._''')

# leitura e set de index do csv
df = pd.read_csv('template_controle.csv')
df = df.set_index(['Data'])

# definição das colunas
col1, col2 = st.columns(spec=2 ,border=True)

tipo = col1.selectbox(label='Escolha o tipo: ', options=['Entrada', 'Saída'])

if tipo == 'Entrada':
    register_entry(df, col1, col2)

    tab_geral, tab_entry, tab_output = st.tabs(['Geral', 'Entradas', 'Saídas'])
    tab_geral.dataframe(df)
    filter_entry(df, tab_entry)
    filter_output(df, tab_output)

else:
    register_output(df, col1, col2)
    
    tab_geral, tab_entry, tab_output = st.tabs(['Geral', 'Entradas', 'Saídas'])
    tab_geral.dataframe(df)
    filter_entry(df, tab_entry)
    filter_output(df, tab_output)