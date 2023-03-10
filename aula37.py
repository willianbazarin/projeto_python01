"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> Quando um código não tem fim
CTRL+C para o programa é so clicar no terminal
"""
condição = True

while condição:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print ('terminou')