"""
ENUNCIADO (Loop While básico)

Abaixo você pode encontrar o exemplo do vídeo onde a 'error' variável, inicialmente igual a 50.0, 
é dividida por 4 e impressa em cada execução:

error = 50.0
while error > 1 :
    error = error / 4
    print(error)

Este exemplo será útil, porque é hora de 'while' você mesmo pode construir um loop! Vamos codificar um loop while 
que implementa um sistema de controle muito básico para um pêndulo invertido. Se houver um deslocamento de ficar
perfeitamente reto, o whileloop corrigirá esse deslocamento incrementalmente. Note que se o seu whileloop demorar 
muito para rodar, você pode ter cometido um erro. Em particular, lembre-se de recuar o conteúdo do loop usando quatro
espaços ou recuo automático!

"""

# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :     ## offset traslate --> desvio
    print("correcting...")
    offset = offset - 1
    print(offset)