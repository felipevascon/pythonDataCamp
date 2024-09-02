"""
ENUNCIADO (Operadores booleanos)

Um booleano pode equivaler ou '1', '0' ou 'True', 'False'. Com operadores booleanos como and, ore not, 
você pode combinar esses booleanos para executar consultas mais avançadas em seus dados.
No código de exemplo, duas variáveis são definidas: 'my_kitchen' e 'your_kitchen', representando áreas.

"""
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen > 3*your_kitchen)