from random import randint
print('{:=^40}'.format(' Pedra Papel Tesoura '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual a sua jogada: "))
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('Opção invalida, tente novamente!')

elif computador == 1:
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Opção invalida, tente novamente!')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção invalida, tente novamente!')