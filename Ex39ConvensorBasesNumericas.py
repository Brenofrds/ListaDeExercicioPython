num = int(input('Escolha um numero inteiro: '))
print('''Escolha uma das opções abaixo:
[1] converter para BINARIO
[2] converter para OCTAGONAL
[3] converter para HEEXAGONAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('O numero {} em binario fica {}'.format(num, bin(num)[2:]))
elif opçao ==2:
    print('O numero {} em octagonal fica {}'.format(num, oct(num)[2:]))
elif opçao ==3:
    print('O numero {} em hexagonal fica {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')
