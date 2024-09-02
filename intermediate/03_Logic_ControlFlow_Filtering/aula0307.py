"""
ENUNCIADO (Filtrando dataframes de Pandas - Parte 2)

O código no exemplo anterior funcionou bem, mas você realmente criou desnecessariamente uma nova variável 'dr'. 
Você pode obter o mesmo resultado sem essa variável intermediária. Coloque o código que calcula 'dr' diretamente 
nos colchetes que selecionam observações de cars.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Convert code to a one-liner
sel = cars[cars['drives_right'].map({'Verdadeiro': True, 'Falso': False})]

# Print sel
print(sel)