"""Calculadora com while"""
"""
while True:
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    print(sair)
"""
    # ou

while True:
    numero_1 = input('digite o 1º número: ')
    numero_2 = input('digite o 2º número: ')
    operador = input('digite o operador a ser executado: + - / * : ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('numeral invalido.')
        continue
    operador_permitidos = '+-/*'
    
    if operador not in operador_permitidos:
        print('operador invalido.')
        continue

    if len(operador) > 1:
        print('Apenas um operador.')
        continue
    
    print('confira o resultado a baixo')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}= ',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}= ',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}= ',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}= ',num_1_float * num_2_float)
       
    else:
        print('algo esta errado!!!!')    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break

