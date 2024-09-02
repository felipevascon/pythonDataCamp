"""
ENUNCIADO (Manipulação de dicionários - Parte 1)

Se você sabe como acessar um dicionário, você também pode atribuir um novo valor a ele. 
Para adicionar um novo par chave-valor, em 'europe' você pode usar algo assim:

europe['iceland'] = 'reykjavik'

"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)