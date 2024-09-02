"""
ENUNCIADO (personalizando com Elif)

Também é possível dar uma olhada no quarto. O código de exemplo contém uma 'elif' que verifica se 'room' é igual a "cama".
Nesse caso, "olhando ao redor no quarto." é impresso. Agora é com você! Faça uma adição semelhante à segunda estrutura de
controle para personalizar ainda mais as mensagens para diferentes valores de area.

"""

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")