'''Faça um programa que jogue par ou impar com o 
computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.'''
from random import randint
vit = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um valor: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(', deu par.' if total % 2 == 0 else ", deu impar.")   
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu')
            vit += 1
        else:
            print('Você Perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu')
            vit += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game Over!! Você venceu {vit} vezes. ')
