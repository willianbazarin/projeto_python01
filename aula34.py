"""
Flag (Bandeira) - Marcar um local
Nome = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

condição = False
passou_no_if = None

if condição:  
   passou_no_if = True
   print('faça algo')
else:
   print('nao faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)