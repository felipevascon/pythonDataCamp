"""
ENUNCIADO (Loop for - Indices e valores)

Usar um forloop para iterar sobre uma lista só lhe dá acesso a cada elemento da lista em cada execução, 
um após o outro. Se você também quiser acessar as informações do índice, então onde o elemento da lista 
sobre o qual você está iterando está localizado, você pode usar enumerate().

Como exemplo, veja como o forloop do vídeo foi convertido:

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("person " + str(index) + ": " + str(height))

Lembre-se: Para pessoas não programadoras, 'room 0: 11.25' é estranho. Certifiquesse de que a coluna room se inicie em 1.

"""
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))