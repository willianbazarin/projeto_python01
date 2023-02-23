# Operadores logicos
# and (e) or (ou) not (não)
# and - Todas as condições precisan ser verdadeiras
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' = False
# Também existe o tipo None que é
# usado para representar uma não valor
entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
 #if so sera interpretador se for verdadeiro, caso nao sera Falsy
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# vai ler ate a afirmativa falsa
print(True and False and True) # Avaliação de curto circuito

