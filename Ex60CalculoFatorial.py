'''Faça um programa que leia um número qualquer e 
mostre o seu fatorial.'''

num = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print('Calculando {}! = '.format(num), end='')
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print('{}'.format(f))
