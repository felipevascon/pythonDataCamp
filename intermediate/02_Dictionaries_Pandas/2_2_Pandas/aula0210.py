"""
ENUNCIADO (Pandas - loc e iloc - Parte 1)

Com 'loce' e 'iloc' você pode fazer praticamente qualquer operação de seleção de dados em DataFrames que você possa imaginar. 
'loc' é baseado em rótulos, o que significa que você tem que especificar linhas e colunas com base em seus rótulos de linha e coluna. 
'iloc' é baseado em índice inteiro, então você tem que especificar linhas e colunas por seus índices inteiros, como você fez no exercício anterior.

Experimente os seguintes comandos no IPython Shell para experimentar 'loc' e 'iloc' selecionar observações. Cada par de comandos aqui dá o mesmo resultado.

cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out observation for Japan
print (cars.loc['JPN'])
print (cars.iloc[2])

# Print out observations for Australia and Egypt
print (cars.loc[['AUS', 'EG']])
print (cars.iloc[[1, 6]])