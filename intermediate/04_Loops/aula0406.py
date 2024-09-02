"""
ENUNCIADO (Loop for - Sobre listas das listas)

Lembra da variável 'house' do curso Introdução ao Python? Dê uma olhada na definição dela no script. 
É basicamente uma lista de listas, onde cada sublista contém o nome e a área de um cômodo da sua casa.

Desta vez , cabe a você construir um forloop do zero!

"""
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for nomeComodo in house :
    areaComodo = str(nomeComodo[1])
    print("the " + nomeComodo[0] + " is " + areaComodo + " sqm")