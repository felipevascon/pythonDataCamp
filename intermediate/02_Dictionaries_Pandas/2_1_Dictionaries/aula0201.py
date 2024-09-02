"""
ENUNCIADO (Dicionários - Criar e acessar elementos dele)

As listas countriese capitalsestão novamente disponíveis no script.
É seu trabalho converter esses dados para um dicionário onde os nomes
dos países são as chaves e as capitais são os valores correspondentes. 
Para relembrar, aqui está uma receita para criar um dicionário:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}

Se as chaves de um dicionário forem escolhidas sabiamente, acessar os valores em um dicionário é fácil e intuitivo.
Por exemplo, para obter a capital da França, 'europe' você pode usar:

europe['france']

"""

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# Print europe
print(europe)

# Print out the keys in europe
print()
print (europe.keys())

# Print out value that belongs to key 'norway'
print (europe['norway'])