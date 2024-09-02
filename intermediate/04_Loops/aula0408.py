"""
ENUNCIADO (Estrutura de dados de Loop - Parte 1 - Loop em matriz numPy)

Se você estiver lidando com uma matriz NumPy 1D, fazer um loop em todos os elementos pode ser tão simples quanto:

for x in my_array :
    ...

Se você estiver lidando com um array NumPy 2D, é mais complicado. Um array 2D é construído de múltiplos arrays 1D. 
Para iterar explicitamente sobre todos os elementos separados de um array multidimensional, você precisará desta sintaxe:

for x in np.nditer(my_array) :
    ...

Duas matrizes NumPy que você pode reconhecer do curso introdutório estão disponíveis na sua sessão Python: np_height, 
uma matriz NumPy contendo as alturas dos jogadores da Major League Baseball, e np_baseball, uma matriz NumPy 2D que contém 
as alturas (primeira coluna) e os pesos (segunda coluna) desses jogadores.

"""
np_height = [74, 74, 72, 72] ##No DataCamp, esta matrize continha multiplos elementos desses

np_baseball = [[74, 180],
            [74, 215],
            [72, 210],
            [75, 205]] ##No DataCamp, esta matrize continha multiplos elementos desses

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height :
    print(str(x), "inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)