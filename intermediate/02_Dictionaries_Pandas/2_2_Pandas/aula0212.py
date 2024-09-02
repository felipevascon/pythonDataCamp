"""
ENUNCIADO (Pandas - loc e iloc - Parte 3)

Também é possível selecionar somente colunas com 'loc' e 'iloc'. Em ambos os casos, 
você simplesmente coloca uma fatia indo do começo ao fim na frente da vírgula:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]

"""

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out drives_right column as Series
print (cars.loc [:, 'drives_right'])

# Print out drives_right column as DataFrame
print (cars.loc [:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print (cars.loc [:, ['cars_per_cap', 'drives_right']])