'''Crie um programa que vai gera cinco números 
aleatórios e colocar em uma tupla. Deois disso, 
mostre a listagem de números gerados e também 
indique o menor e o maior valor que estão na tupla.'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10),)
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')