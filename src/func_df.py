import pandas as pd

def salvar_df(dict_data,df):
    df = pd.concat([df, pd.DataFrame.from_dict([dict_data])],axis=0, ignore_index=True)
    df.to_csv('template_controle.csv', sep=',')
    print(f'\n{dict_data['Tipo']} : {dict_data['Descrição']} - {dict_data['Data']}\nAdicionado.')