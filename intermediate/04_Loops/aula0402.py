"""
ENUNCIADO (Loop While com condicionais)

O whileloop que corrige o offset é um bom começo, mas e se offsetfor negativo? Você pode tentar executar
o seguinte código onde offsetis initialized to -6:

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)

No entanto, sua sessão será desconectada. O whileloop nunca parará de rodar, porque offsetserá diminuído ainda 
mais a cada execução. offset != 0 nunca se tornará False e o whileloop continuará para sempre. Corrija as coisas 
colocando uma declaração if- else dentro do whileloop. Se seu código ainda estiver demorando muito para rodar, 
você provavelmente cometeu um erro!

"""
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)