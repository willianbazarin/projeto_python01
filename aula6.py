# conversao de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converterum tipo em outro 
# tipos imutaveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) #converteu str em int
print('1')
# print('1' + 1) # nesta esta dara erro type, pois pe uma str + int, o correto é int+int
# para converter
print(int('1') + 1) # converteu e conseguiu somar
print(float('1') + 3.0)
print(type(float('1')+ 1))
print(bool('')) # sem bool sem espaço é False
print(bool(' '))# com bool com espaço é True
print(bool('1242' == '222'))
print(str(11) + 'b')



