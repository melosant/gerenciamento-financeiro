import streamlit as st
import pandas as pd

def register_entry(df, col_e, col_d):
    '''
    função de que armazena as entradas
    e por fim, as salva no csv
    
    :param df: dataframe
    :param col_e: coluna da esquerda
    :param col_d: coluna da direita
    '''
    data = col_e.date_input('Selecione a data:', format='DD/MM/YYYY')
    valor = col_d.number_input('Digite o valor (R$):')
    desc = col_d.text_input('Digite uma breve descrição da entrada:')
    registro = st.button('Registrar')

    if registro:
        data_set = {
            'Data': [data],
            'Valor': [valor],
            'Tipo': ['ENTRADA'],
            'Desc': [desc]}

        save_register_csv(df, data_set)


def register_output(df, col_e, col_d):
    '''
    função de que armazena as saídas
    e por fim, as salva no csv
    
    :param df: dataframe
    :param col_e: coluna da esquerda
    :param col_d: coluna da direita
    '''
    data = col_e.date_input('Selecione a data:', format='DD/MM/YYYY')
    valor = col_d.number_input('Digite o valor (R$):')
    desc = col_d.text_input('Digite uma breve descrição da saída:')
    registro = st.button('Registrar')

    if registro:
        data_set = {
            'Data': [data],
            'Valor': [valor],
            'Tipo': ['SAÍDA'],
            'Desc': [desc]}

        save_register_csv(df, data_set)


def save_register_csv(df, data_set):
    '''
    Função que concatena o csv principal com o registro atual e os salva no csv. 
    
    :param df: dataframe
    :param dados: dicionario com a entrada/saida registrada
    '''
    data_set = pd.DataFrame.from_dict(data_set)
    data_set = data_set.set_index(['Data'])
    df = pd.DataFrame(df)
    df = pd.concat([df, data_set], axis=0) 
    df.to_csv('finp.csv')

    st.badge('Registro adicionado com sucesso.', color='green')
    st.dataframe(data_set) 

def filter_entry(df, tab):
    '''
    função que filtra somente as entradas
    
    :param df: dataframe
    :param tab: aba
    '''
    filtro_entry = df['Tipo'] == 'ENTRADA'
    df_entry = df[filtro_entry]
    tab.dataframe(df_entry)

def filter_output(df, tab):
    '''
    função que filtra somente as saídas
    
    :param df: dataframe
    :param tab: aba
    '''
    filtro_entry = df['Tipo'] == 'SAÍDA'
    df_entry = df[filtro_entry]
    tab.dataframe(df_entry)