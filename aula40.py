"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""
contador = 0


while contador <= 100:
    contador += 1
    
    if contador == 6:
        print (contador) #usando para pular algum termo
        continue
    

    if contador >= 10 and contador <=30:
        print('pulou do 10 ao 30')
        continue
    
    
    print (contador)
    
    
    if contador == 50:
        break
print ('Acabou')

