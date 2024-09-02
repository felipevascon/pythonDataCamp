"""
ENUNCIADO (Pandas - Dicionário para DataFrame - Parte 1)

Pandas é uma biblioteca de código aberto, que fornece estruturas de dados e ferramentas de análise de dados de alto desempenho e fáceis de usar para Python.
O DataFrame é uma das estruturas de dados mais importantes do Pandas. É basicamente uma maneira de armazenar dados tabulares onde você pode rotular as linhas
e as colunas. Uma maneira de construir um DataFrame é a partir de um dicionário. Nos exercícios a seguir, você trabalhará com dados de veículos de diferentes países. 
Cada observação corresponde a um país e as colunas dão informações sobre o número de veículos per capita, se as pessoas dirigem para a esquerda ou para a direita, 
e assim por diante.

Três listas são definidas no script:

names --> contendo os nomes dos países para os quais há dados disponíveis.
dr --> uma lista com valores booleanos que informa se as pessoas dirigem para a esquerda ou para a direita no país correspondente.
cpc --> o número de veículos motorizados por 1000 pessoas no país correspondente.

Cada chave de dicionário é um rótulo de coluna e cada valor é uma lista que contém os elementos da coluna.

"""
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame (my_dict)

# Print cars
print (cars)