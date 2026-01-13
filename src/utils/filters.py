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

    # um df novo recebe uma cópia para formatar a coluna valor
    df_entry_format = df_entry.copy()
    df_entry_format['Valor'] = df_entry_format['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))

    if len(df_entry_format) == 0:
        st.warning('Nenhuma entrada registrada na base de dados.')
    else: 
        tab.dataframe(df_entry_format)

    return df_entry

def filter_output(df, tab):
    '''
    função que filtra somente as saídas
    
    :param df: dataframe
    :param tab: aba
    '''
    filtro_output = df['Tipo'] == 'SAÍDA'
    df_output = df[filtro_output]

    # um df novo recebe uma cópia para formatar a coluna valor
    df_out_format = df_output.copy()
    df_out_format['Valor'] = df_out_format['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))

    if len(df_out_format) == 0:
        st.warning('Nenhuma saída registrada na base de dados.')
    else: 
        tab.dataframe(df_out_format)

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

    # um df novo recebe uma cópia para formatar a coluna valor
    df_formatado_mes = df_filtrado_mes.copy()
    df_formatado_mes['Valor'] = df_formatado_mes['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))

    if escolha:
        tab.dataframe(df_formatado_mes)
    else:
        tab.warning('Nada registrado na base de dados FINP.')

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

    # um df novo recebe uma cópia para formatar a coluna valor
    df_formatado_ano = df_filtrado_ano.copy()
    df_formatado_ano['Valor'] = df_formatado_ano['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ','))

    if escolha:
        tab.dataframe(df_formatado_ano)
    else:
        tab.warning('Nada registrado na base de dados FINP.')

    return df_filtrado_ano