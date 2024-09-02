"""
ENUNCIADO (Estrutura de dados de Loop - Parte 1 - Loop em dicionário)

No Python 3, você precisa da funcao items() para fazer um loop em um dicionário:

world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))

Lembra do dicionario 'europe' que continha os nomes de alguns países europeus como 
chave e suas capitais como valor correspondente? Vá em frente e escreva um loop 
para iterar sobre ele!

"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() :
     country = str(key)
     capital = str(value)
     print("the capital of " + country + " is " + capital)