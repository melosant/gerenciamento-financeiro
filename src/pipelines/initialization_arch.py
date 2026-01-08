import pandas as pd
import streamlit as st

def archive_initialization():
    '''
    Verifica se o arquivo existe e o inicia
    '''
    
    if not archive_exist():
        create_csv()
        st.success('Base de Dados FINP Criada.')
    else:
        st.warning('Base de Dados Iniciada.')

def archive_exist():
    '''
    caso consiga abrir e fechar o arquivo, confirma a existência
    '''
    try:
        a = open('finp.csv', 'r')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
    
def create_csv():
    '''
    cria a base de dados com as colunas já especificadas
    '''
    columns = ['Data', 'Valor', 'Tipo', 'Desc']
    dataframe = pd.DataFrame(columns=columns)
    dataframe = dataframe.set_index(['Data'])
    dataframe.to_csv('finp.csv')