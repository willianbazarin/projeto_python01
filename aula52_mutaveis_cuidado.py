"""
Cuidados com dados mutáveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na mémoria (mutável)
"""
lista_a = ['Luiz','Maria']
lista_b = lista_a


lista_a [0] = 'Qualquer coisa'
print(lista_b)