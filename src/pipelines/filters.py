import streamlit as st
import pandas as pd

def filter_entry(df, tab):
    '''
    função que filtra somente as entradas
    
    :param df: dataframe
    :param tab: aba
    '''
    filtro_entry = df['Tipo'] == 'ENTRADA'
    df_entry = df[filtro_entry]
    if len(df_entry) == 0:
        st.warning('Nenhuma entrada registrada na base de dados.')
    else: 
        tab.dataframe(df_entry)

    return df_entry

def filter_output(df, tab):
    '''
    função que filtra somente as saídas
    
    :param df: dataframe
    :param tab: aba
    '''
    filtro_output = df['Tipo'] == 'SAÍDA'
    df_output = df[filtro_output]
    if len(df_output) == 0:
        st.warning('Nenhuma saída registrada na base de dados.')
    else: 
        tab.dataframe(df_output)

    return df_output

def filter_month(df, tab):
    '''
    cria um df filtrado pelo mês que o usuário selecionar
    
    :param df: dataframe
    :param tab: aba utilizada
    '''
    meses = pd.to_datetime(df.index).month
    meses_unicos = meses.unique()
    escolha = tab.selectbox(label='Selecione o mês que deseja ver o resumo:', options=meses_unicos)
    filtro = (meses == escolha)
    df_filtrado_mes = df[filtro]

    tab.dataframe(df_filtrado_mes)

    return df_filtrado_mes

def filter_year(df, tab):
    '''
    cria um df filtrado pelo ano que o usuário selecionar
    
    :param df: dataframe
    :param tab: aba utilizada
    '''
    anos = pd.to_datetime(df.index).year
    anos_unicos = anos.unique()
    escolha = tab.selectbox(label='Selecione o ano que deseja ver o resumo:', options=anos_unicos)
    filtro = (anos == escolha)
    df_filtrado_ano = df[filtro]

    tab.dataframe(df_filtrado_ano)

    return df_filtrado_ano