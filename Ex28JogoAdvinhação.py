import random
import time
print('Eu computador vou pensar em um numero de 0 a 5, tente adivinhar qual numero eu pensei')
NumJogador = int(input("Em qual numero eu pensei: "))
NumComputador = random.randint(0, 5)
print('Processando...')
time.sleep(2)
if NumJogador == NumComputador:
    print('Voce acertooou!!')
else:
    print('Voce errou, tente novamente!')