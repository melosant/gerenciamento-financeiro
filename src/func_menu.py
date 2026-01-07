import pandas as pd
from src.func_df import salvar_df

def register_entry():
    date = input('Digite a data da entrada (dd/mm/aaaa): ')
    valor = float(input('Digite o valor da entrada: R$'))
    desc = input('Digite uma breve descrição: ')

    dict_data = {
        'Data': date,
        'Valor': valor,
        'Tipo': 'ENTRADA',
        'Descrição': desc,
    }
    return dict_data

def register_output():
    date = input('Digite a data da saída (dd/mm/aaaa): ')
    valor = float(input('Digite o valor da saída: R$'))
    desc = input('Digite uma breve descrição: ')

    dict_data = {
        'Data': date,
        'Valor': valor,
        'Tipo': 'SAÍDA',
        'Descrição': desc,
    }
    return dict_data

def main_function(dataframe):
    try:
        tipo = int(input('[1] - ENTRADA\n[2] - SAÍDA\n[3] - SAIR DO SISTEMA\nDIGITE SUA OPÇÃO: '))
    except ValueError:
        print('\nDIGITE UMA OPÇÃO NÚMERICA VÁLIDA.')
    except KeyboardInterrupt:
        print('\nSAINDO DO SISTEMA...')
    except Exception as e:
        print('\nERRO:', e.__class__.__name__)
    else:
        if tipo == 1:
            dados = register_entry()
            salvar_df(dados, dataframe)

        elif tipo == 2:
            dados = register_output()
            salvar_df(dados, dataframe)

        elif tipo == 3:
            print('\nSAINDO DO SISTEMA...')

        else:
            print('\nDIGITE UMA OPÇÃO VÁLIDA [1-3].')