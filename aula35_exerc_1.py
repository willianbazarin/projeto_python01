"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
Valor = input('digite um numero inteiro:')


if Valor.isdigit():
     Valor_int = int(Valor)
     par_impar = Valor_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {Valor_int} é {par_impar_texto}')
else:
     print('Você não digitou um número inteiro')





#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
