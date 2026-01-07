import pandas as pd
import streamlit as st

def archive_initialization():
    if not archive_exist():
        create_csv()
        st.badge('Base de Dados FINP Criada.', color='green')
    else:
        st.badge('Base de Dados Iniciada.', color='yellow')

def archive_exist():
    try:
        a = open('finp.csv', 'r')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
    
def create_csv():
    columns = ['Data', 'Valor', 'Tipo', 'Desc']
    dataframe = pd.DataFrame(columns=columns)
    dataframe = dataframe.set_index(['Data'])
    dataframe.to_csv('finp.csv')