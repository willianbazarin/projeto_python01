"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 70 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A DISTANCIA ONDE O RADAR PEGA
# QUANDO A VARIAVEL ESTIVER EM MAIUSCULO É UMA VARIAVEL PARA NAO SER FEITA ALTERAÇÃO
# pode se fazer uma variavel para deixa o codigo mais simples, exemplo:
velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
# F2 PARA MUDAR TODA A VARIAVEL, COM O CURSOU DO MOUSE


if velocidade_carro_passou_radar_1:
    print ('velocidade carro passou do radar 1')

if carro_passou_radar_1 and velocidade_carro_passou_radar_1:
    print ('carro multado em radar 1')

if RADAR_1 >= velocidade_carro_passou_radar_1:
    print('passou dentro da velocidade')
