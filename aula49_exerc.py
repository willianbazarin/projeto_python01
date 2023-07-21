"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voçê vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuario digitar apenas uma letra.
- Qaundo o ususario digitar uma letra, voçê vai conferir se a letra 
digitada esta na palavra secreta.
        - Se a letra digitada estiver na palavra secreta: exiba a letra;
        - Se a letra digitada não estiver na palavra secreta: exiba *.
Faça a contagem de tentativas do seu usuario
"""
import os

palavra_secreta = 'gostosona'
letras_acerdatas = ''
numero_tentativa = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite anenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acerdatas += letra_digitada
    
    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acerdatas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print ('VOCE GANHOU!!!')
        print('A palavra era: ', palavra_secreta)
        print('Numero de tentativas: ', numero_tentativa)    
        letras_acerdatas = ''
        numero_tentativa = 0