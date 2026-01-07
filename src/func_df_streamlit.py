import streamlit as st
import pandas as pd

def register_entry(df, col_e, col_d):
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


def save_register_csv(df, dados):
    dados = pd.DataFrame.from_dict(dados)
    dados = dados.set_index(['Data'])
    df = pd.DataFrame(df)
    df = pd.concat([df, dados], axis=0) 
    df.to_csv('template_controle.csv', sep=',')

    st.badge('Adicionado com sucesso.', color='green', width='content')

def filter_entry(df, tab):
    filtro_entry = df['Tipo'] == 'ENTRADA'
    df_entry = df[filtro_entry]
    tab.dataframe(df_entry)

def filter_output(df, tab):
    filtro_entry = df['Tipo'] == 'SAÍDA'
    df_entry = df[filtro_entry]
    tab.dataframe(df_entry)