"""
Listas em Python 
tipo list - mutavel
suporta varios valoes de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
"""
#lista = [] #pode ser apenas abrindo o[]
#print  (boot([])) # falsy

lista = [123, True, 'Willian Bazarin', 1.2, []]
print(lista[2])
print(lista[2].upper(), type(lista[2]))
# é possivel trocar apenas o termo que se quer na lista
# exemplo: 
lista = [123, True, 'Bazarin', 1.2, []]
lista[-3] = 'Silva'
print(lista[2])
print(lista[2].upper(), type(lista[2]))


