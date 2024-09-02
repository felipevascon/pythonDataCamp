"""
ENUNCIADO (Manipulação de dicionários - Parte 2)

Uma versão adaptada do europedicionário está disponível no script. Você pode limpar? 
Não faça isso adaptando a definição de 'europe', mas adicionando comandos Python ao script
para atualizar e remover pares 'chave:valor'.

"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del europe['australia']

# Print europe
print (europe)