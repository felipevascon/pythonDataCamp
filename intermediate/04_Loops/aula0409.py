"""
ENUNCIADO (Estrutura de dados de Loop - Parte 2 - Loop em DataFrame (1))

A iteração sobre um Pandas DataFrame é normalmente feita com a funcao 'iterrows()'. 
Usada em um forloop, cada observação é iterada e em cada iteração o rótulo da linha 
e o conteúdo real da linha estão disponíveis:

for lab, row in brics.iterrows() :
    ...

Neste e nos exercícios seguintes, você trabalhará no dataFrame 'cars'. Ele contém informações 
sobre os carros per capita e se as pessoas dirigem para a direita ou para a esquerda em sete países do mundo.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)