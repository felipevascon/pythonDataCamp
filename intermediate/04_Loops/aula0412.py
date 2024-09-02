"""
ENUNCIADO (Estrutura de dados de Loop - Parte 2 - Add coluna (2))

Usar 'iterrows()' para iterar sobre cada observação de um Pandas DataFrame é fácil de entender, mas não muito eficiente. 
Em cada iteração, você está criando uma nova Pandas Series. Se você quiser adicionar uma coluna a um DataFrame chamando 
uma função em outra coluna, a funcao 'iterrows()' em combinação com um forloop não é a maneira preferida de fazer isso. 
Em vez disso, você vai querer usar apply().

Compare a 'iterrows()' versão com a 'apply()' versão para obter o mesmo resultado no bricsDataFrame:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)

Podemos fazer algo similar para chamar o 'upper()' método em cada nome na coluna 'country'. No entanto, upper()é um método, 
então precisaremos de uma abordagem um pouco diferente:

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)