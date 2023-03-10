a = 'A'
b = 'B'
c = 1.1
#formato = 'a={} b={}'. format(a, b, c)  da certo ou
string = 'a={} b={} c={nome3:.2f}'

formato = string.format(a, b, nome3=c)

print (formato)

# out of ranger = erro que pode aconteceu quando é pedido para executar algum argumento que 
# ja finalizou. 
# formato = string.format(a, b, mone3c) = parametro nome adotem que colocar em todos
# 