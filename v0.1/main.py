import pandas as pd
from src.func_menu import main_function
df = pd.read_csv('template_controle.csv', index_col=0)

main_function(df)