"""
ENUNCIADO (Pandas - Colchetes - Parte 2)

Colchetes podem fazer mais do que apenas selecionar colunas. Você também pode usá-los para obter linhas, ou observações, de um DataFrame.
A chamada a seguir seleciona as cinco primeiras linhas do carsDataFrame:

cars[0:5]

O resultado é outro DataFrame contendo apenas as linhas que você especificou.

Preste atenção: Você só pode selecionar linhas usando colchetes se especificar uma fatia, como 0:4. Além disso, você está usando os índices
inteiros das linhas aqui, não os rótulos das linhas!

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out first 3 observations
print (cars[0:3])

# Print out fourth, fifth and sixth observation
print (cars[3:6])