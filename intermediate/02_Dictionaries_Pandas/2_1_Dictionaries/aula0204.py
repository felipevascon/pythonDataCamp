"""
ENUNCIADO (Dicionarirecepcão)

Lembra das listas? Elas podem conter qualquer coisa, até mesmo outras listas. 
Bem, para dicionários o mesmo vale. Dicionários podem conter pares 'chave:valor' 
onde os valores são novamente dicionários. Como exemplo, dê uma olhada no script 
onde outra versão de 'europe' - o dicionário com o qual você tem trabalhado o tempo todo - está codificada.
As chaves ainda são os nomes dos países, mas os valores são dicionários que contêm mais informações do que apenas a capital.

É perfeitamente possível encadear colchetes para selecionar elementos. Para buscar a população da Espanha de europe, por exemplo, 
você precisa:

europe['spain']['population']

"""

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
europe['france']['capital']

# Create sub-dictionary data
data = {'capital':'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print (europe)