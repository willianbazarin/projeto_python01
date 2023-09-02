"""
Introdução ao desempacotamento + tuples (tuplas)
"""
#nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes

nome1, *_ = ['Maria', 'Helena', 'Luiz']

print(nome1)


_, nome2, *_ = ['Maria', 'Helena', 'Luiz']

print(nome2)