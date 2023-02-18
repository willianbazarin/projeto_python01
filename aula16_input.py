nome = input('qual seu nome? ')
print(f'meu nome é: {nome}')

numero_1 = input('Digite o primeiro numero:')
numero_2 = input('Digite o segundo numero:')
# se for converter o input para numero, pois ele por natureza ja é um str,
# executando da seguinte maneira podera dar erro e o programador nao sabera o que 
# foi digitado é -> int(input('Digite o primeiro numero')) mas se fazer da seguinte
# forma fica um pouco maior mas sera possivel saber o que foi escrito
# e assim descobri o erro
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos numeros é: {int_numero_1 + int_numero_2} ')
print (type (int_numero_1))
