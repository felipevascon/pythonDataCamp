"""
ENUNCIADO (Pandas - Colchetes - Parte 1)

No vídeo, você viu que pode indexar e selecionar Pandas DataFrames de muitas maneiras diferentes. 
A mais simples, mas não a mais poderosa, é usar colchetes. No código de exemplo, os mesmos dados de
carros são importados de um arquivo CSV como um Pandas DataFrame. Para selecionar apenas a 'cars_per_cap' 
coluna de cars, você pode usar:

cars['cars_per_cap']
cars[['cars_per_cap']]

A versão com colchetes simples fornece uma Pandas Series, a versão com colchetes duplos fornece um Pandas DataFrame.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])