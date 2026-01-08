import streamlit as st
import pandas as pd
from src.pipelines.register import register_entry, register_output
from src.pipelines.initialization_arch import archive_initialization

# verificação da existência da base da dados
archive_initialization()

st.title('Sistema FINP')
st.markdown('''_Pressione "R" para atualizar a página e as tabelas._''')

# leitura e set de index do csv
df = pd.read_csv('finp.csv')
df = df.set_index(['Data'])

# definição das colunas
col1, col2 = st.columns(spec=2 ,border=True)

tipo = col1.selectbox(label='Escolha o tipo: ', options=['Entrada', 'Saída'])

if tipo == 'Entrada':
    register_entry(df, col1, col2)
else:
    register_output(df, col1, col2)
