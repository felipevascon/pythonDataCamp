"""
ENUNCIADO (Pandas - Dicionário para DataFrame - Parte 2)

O código Python que resolve o exercício anterior está incluído no script. Você notou que os rótulos de linha 
(ou seja, os rótulos para as diferentes observações) foram automaticamente definidos como inteiros de 0 a 6?
Para resolver isso, uma lista 'row_labels' foi criada. Você pode usá-la para especificar os rótulos de linha 
do carsDataFrame. Você faz isso definindo o 'index' atributo de 'cars', que você pode acessar como 'cars.index'.

"""
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)