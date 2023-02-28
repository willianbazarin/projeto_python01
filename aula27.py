"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x OU X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o numero a aparecer antes dos zeros
sinal - + ou -
ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel:*^10}.')
print(f'{1000.123415432154312:.1f}')
print('O hexadecimal de %d é %x' % (15, 15)) # interpolação
print(f'O hexadecimal de 15 é {15:01x}') # f-string (qualquer uma que usar faz a mesma coisa)

      



