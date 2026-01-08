def total_entry(df, tab, col1):

    filtro = df['Tipo'] == 'ENTRADA'
    df_entry = df[filtro]
    total_entrada = sum(df_entry['Valor'])
    with tab:
        col1.markdown(f'Total de Entradas: R$ {total_entrada}', text_alignment='center')

    return total_entrada

def total_outputs(df, tab, col2):

    filtro = df['Tipo'] == 'SAÍDA'
    df_outputs = df[filtro]
    total_saida = sum(df_outputs['Valor'])
    with tab:
        col2.markdown(f'Total de Saídas: R$ {total_saida}', text_alignment='center')

    return total_saida

def difference(df, tab, col1, col2):

    entrada_total = total_entry(df, tab, col1)
    saida_total = total_outputs(df, tab, col2)
    diferenca = entrada_total - saida_total
    cont = tab.container(border=True)
    cont.markdown(f'Saldo Total: R$ {diferenca}', text_alignment='center')