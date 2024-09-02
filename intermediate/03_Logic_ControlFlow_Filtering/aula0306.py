"""
ENUNCIADO (Filtrando dataframes de Pandas - Parte 1)

Lembra daquele conjunto de dados 'cars.csv' contendo os carros por 1000 pessoas (cars_per_cap) 
e se as pessoas dirigem corretamente (drives_right) para diferentes países (country)? O código 
que importa esses dados em formato CSV para o Python como um DataFrame está incluído no script.
No vídeo, você viu uma abordagem passo a passo para filtrar observações de um DataFrame com base
em matrizes booleanas. Vamos começar de forma simples e tentar encontrar todas as observações em 
cars onde drives_right é True.

'drives_right' é uma coluna booleana, então você terá que extraí-la como uma Série e então usar essa
série booleana para selecionar observações de cars.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Extract drives_right column as Series: dr
dr = cars["drives_right"].map({'Verdadeiro': True, 'Falso': False})

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)