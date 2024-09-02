"""
ENUNCIADO (Operadores booleanos com NumPy)

Antes, os operadores operacionais '<' e '>=' trabalhavam com arrays NumPy prontos para uso. 
Isso não é verdade para os operadores booleanos and, or, e not. Para usar esses operadores com NumPy,
você precisará de 'np.logical_and()', 'np.logical_or()' e 'np.logical_not()'. Aqui está um exemplo nos arrays 
'my_house' e 'your_house' de antes para lhe dar uma ideia:

np.logical_and(my_house > 13, 
               your_house < 15)

"""

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))