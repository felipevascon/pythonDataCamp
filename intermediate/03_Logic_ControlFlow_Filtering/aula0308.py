"""
ENUNCIADO (Cars per capita - Parte 1)

Vamos nos ater aos 'cars' dados um pouco mais. Desta vez, você quer descobrir quais países têm um alto número de carros per capita.
Em outras palavras, em quais países muitas pessoas têm um carro, ou talvez vários carros. Semelhante ao exemplo anterior, você vai 
querer construir uma Series booleana, que você pode então usar para subconjunto do carsDataFrame para selecionar certas observações. 
Se você quiser fazer isso em uma linha, está perfeitamente bem!

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print (car_maniac)