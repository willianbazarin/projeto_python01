"""
enimerate - enumera iteraveis(indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

lista_enumerada = enumerate(lista)# esta função para 
#print (lista_enumerada) se deixa assim vai da erro, pode ser usado da seguinte forma:
for item in lista_enumerada:
    print(item) 
