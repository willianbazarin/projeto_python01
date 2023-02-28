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
nome = input('Digite seu nome: ')
idade = input ('Digite sua idade: ')

if nome and idade:
    print (f'seu nome é: {nome}')
    print (f'sua idade e: {idade}')
    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')

    print (f'seu nome invertido é:', nome[::-1])
    print (f'seu nome tem [n] caracteres:', len (nome))
    print (f'a primeira letra de seu nome é:', nome[0])
    print (f'a primeira letra de seu nome é:', nome[-1])