"""
ENUNCIADO (Pandas - CSV para DataFrame)

Colocar dados em um dicionário e então construir um DataFrame funciona, mas não é muito eficiente. 
E se você estiver lidando com milhões de observações? Nesses casos, os dados geralmente estão disponíveis
como arquivos com uma estrutura regular. Um desses tipos de arquivo é o arquivo CSV, que é a abreviação de 
"valores separados por vírgula". Para importar dados CSV para Python como um Pandas DataFrame, você pode usar read_csv().

Vamos explorar essa função com os mesmos dados de carros dos exercícios anteriores. Desta vez, no entanto, os dados estão
disponíveis em um arquivo CSV, chamado cars.csv. Ele está disponível no seu diretório de trabalho atual, então o caminho 
para o arquivo é simplesmente 'cars.csv'.

Lembre-se de incluir o index_col, um argumento de read_csv(), que você pode usar para especificar qual coluna no arquivo CSV 
deve ser usada como um rótulo de linha.

"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(r'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\cars.csv', index_col = 0) #caminho do arquivo CSV será alterado caso seja acessado de outra máquina

# Print out cars
print (cars)