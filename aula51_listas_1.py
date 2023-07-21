"""
Listas em Python 
tipo list - mutavel
suporta varios valoes de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""
lista = [1, 2, 3, 4, 5]
lista [2] = 300
numero = lista[2]
#del lista[2]

print (lista)
#print (lista[2])
# para adicionar valor no final da lista
lista.append(10)
#lista.pop() # remove o ultimo da lista
lista.append(50)
ultimo_valor = lista.pop()

print(lista, 'removido ', ultimo_valor )
