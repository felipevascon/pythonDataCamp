"""
ENUNCIADO (Comparação de matrizes)

Pronto para uso, você pode usar operadores de comparação com matrizes NumPy.
Lembra-se 'areas' da lista de medidas de área para diferentes cômodos da sua casa da Introdução ao Python? 
Desta vez, há dois arrays NumPy: 'my_house' e 'your_house'. Ambos contêm as áreas da cozinha, sala de estar, 
quarto e banheiro na mesma ordem, para que você possa compará-los.

"""

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house <= your_house)