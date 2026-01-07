import pandas as pd

def salvar_df(dict_data,df):
    df = pd.concat([df, pd.DataFrame.from_dict([dict_data])],axis=0, ignore_index=True)
    df.to_csv('template_controle.csv', sep=',')
    print(f'\n{dict_data['Tipo']} : {dict_data['Descrição']} - {dict_data['Data']}\nAdicionado.')

def filter_entry(dataframe):
    filtro_entry = dataframe['Tipo'] == 'ENTRADA'
    df_entry = dataframe[filtro_entry]
    df_entry = df_entry.drop('Unnamed: 0', axis=1)
    print(df_entry)
    print(f'\nTOTAL ENTRADA: R${sum(df_entry['Valor'])}\n')

def filter_outputs(dataframe):
    filtro_outputs = dataframe['Tipo'] == 'SAÍDA'
    df_output = dataframe[filtro_outputs]
    df_output = df_output.drop('Unnamed: 0', axis=1)
    print(df_output)
    print(f'\nTOTAL SAÍDA: R${sum(df_output['Valor'])}\n')