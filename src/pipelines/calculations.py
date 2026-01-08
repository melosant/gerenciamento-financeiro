def total_entry(df, tab, col1):
    '''
    Calcula o total de entradas nos df's filtrados
    
    :param df: dataframe filtrado
    :param tab: aba utilizada
    :param col1: coluna
    '''
    filtro = df['Tipo'] == 'ENTRADA'
    df_entry = df[filtro]
    total_entrada = sum(df_entry['Valor'])
    with tab:
        col1.markdown(f'Total de Entradas: R$ {total_entrada}', text_alignment='center')

    return total_entrada

def total_outputs(df, tab, col2):
    '''
    Calcula o total de saídas nos df's filtrados
    
    :param df: dataframe filtrado
    :param tab: aba utilizada
    :param col1: coluna
    '''
    filtro = df['Tipo'] == 'SAÍDA'
    df_outputs = df[filtro]
    total_saida = sum(df_outputs['Valor'])
    with tab:
        col2.markdown(f'Total de Saídas: R$ {total_saida}', text_alignment='center')

    return total_saida

def difference(df, tab, col1, col2):
    '''
    Calcula a diferença entre as entradas e as saídas registradas no df filtrado
    
    :param df: dataframe filtrado
    :param tab: aba utilizada
    :param col1: coluna da esquerda
    :param col2: coluna da direita
    '''
    entrada_total = total_entry(df, tab, col1)
    saida_total = total_outputs(df, tab, col2)
    diferenca = entrada_total - saida_total
    cont = tab.container(border=True)
    cont.markdown(f'Saldo Total: R$ {diferenca}', text_alignment='center')