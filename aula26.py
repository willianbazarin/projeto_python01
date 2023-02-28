"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Willian'
preço = 1000.95897643
variavel = '%s, o preço é R$%.7f' % (nome, preço)
print(variavel)
# s= string no lugar de usar {}
print('Ohexadecimal de %d é %x' % (15, 15))