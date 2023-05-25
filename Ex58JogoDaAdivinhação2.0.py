'''O computador vai pensar em um numero entre 0 e 10. 
Só que agora o jogador vai tentar advinhar até 
acertar, mostrando no final quantos palpites foram 
necessários para vencer'''
import random
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi?')
aleatorio = random.randint(0,10)
num = 11
tentativas = 0
while aleatorio != num:
    num = int(input('Qual o seu papalpite: '))
    if aleatorio != num and aleatorio > num:
        print("Errou... mais um pouquinho")
    if aleatorio != num and aleatorio < num:
        print('Errou... menos um pouquinho')
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))