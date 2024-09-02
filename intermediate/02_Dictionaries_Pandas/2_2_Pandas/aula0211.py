"""
ENUNCIADO (Pandas - loc e iloc - Parte 2)

'loc' e 'iloc' também permite que você selecione linhas e colunas de um DataFrame. Para experimentar,
experimente os seguintes comandos no IPython Shell. Novamente, comandos pareados produzem o mesmo resultado:

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]

"""

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out drives_right value of Morocco
print (cars.loc['MOR', 'drives_right'])
# or (cars.iloc[5, 2])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
# or print(cars.iloc[[4,5], [1,2]])