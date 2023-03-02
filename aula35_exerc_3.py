"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu nome:')
tamanho_nome = len (nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print ('seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6: #tomar cuidado if junto executa junto 2 enter
        print('Seu nome é normal') # por isso colocar o elif se usar o if basta separar
    else:
        print(' seu nome é grande')
else:
    print('digite pelo menos uma letra')