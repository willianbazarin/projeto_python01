# Operadores logicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeiro. 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' = False
# Também existe o tipo None que é
# usado para representar uma não valor
entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
 #if so sera interpretador se for verdadeiro, caso nao sera Falsy
senha_permitida = '123456'
# para acrescentar pode colocar entre ()
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('adentrar')
else:
    print('Sair')

# vai ler ate a afirmativa falsa
print(True and 0 and True) # Avaliação de curto circuito
print(0 or False or 0 or 'abc' or True) # sera levado em consideração o prim. valor verdadeiro
# 
senha = input ('senha: ') or 'Sem senha'
print (senha)

