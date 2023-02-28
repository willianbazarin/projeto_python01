"""
Exercício
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome contém (ou não) espaços ***
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba " Desculpe, voê deixou campos vazios. 
"""
nome_usuario = input('Digite seu nome: ')
idade = input ('Digite sua idade: ')
variavel = (f'{nome_usuario}')

if nome_usuario:
    print (f'seu nome é: {nome_usuario}')
    print (f'sua idade e: {idade}')
    if ' ' in nome_usuario:
        print('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')
    print (f'seu nome invertido é:', variavel[::-1])
    print (f'seu nome tem [n] caracteres:', len (variavel))
    print (f'a primeira letra de seu nome é:', variavel[0])
    print (f'a primeira letra de seu nome é:', variavel[-1])
else:
    print('nome e idade nao digitado')
