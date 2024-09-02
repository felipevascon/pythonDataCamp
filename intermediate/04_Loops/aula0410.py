"""
ENUNCIADO (Estrutura de dados de Loop - Parte 2 - Loop em DataFrame (2))

Os dados de linha gerados por 'iterrows()' em cada execução são uma Pandas Series. 
Este formato não é muito conveniente para imprimir. Felizmente, você pode selecionar 
facilmente variáveis Pandas Series usando colchetes:

for lab, row in brics.iterrows() :
    print(row['country'])

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))