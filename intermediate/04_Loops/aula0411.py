"""
ENUNCIADO (Estrutura de dados de Loop - Parte 2 - Add coluna (1))

No vídeo, Hugo mostrou como adicionar o comprimento dos nomes dos países do bricsDataFrame em uma nova coluna:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

Você pode fazer coisas semelhantes no 'cars' DataFrame.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)