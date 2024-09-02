"""
ENUNCIADO (Cars per capita - Parte 2)

Lembra sobre 'np.logical_and()', 'np.logical_or()' e 'np.logical_not()' como variantes NumPy dos operadores and, ore not? 
Você também pode usá-los no Pandas Series para fazer operações de filtragem mais avançadas. Veja este exemplo que seleciona
as observações que têm 'cars_per_cap' entre 10 e 80. Experimente estas linhas de código passo a passo para ver o que está acontecendo.

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)