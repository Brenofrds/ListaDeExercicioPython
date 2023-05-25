'''Faça um programa que leia 5 valores númerico e 
guarde-os em uma lista. No final, mostre qual foi o 
maior e o menor valor digitado e suas respectivas 
posições na lista.'''

lista = []
maior = menor = 0

for i in range(0,5):
    lista.append(int(input(f'Digite o valor na posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

print(f'Você digitou os números {lista}')
print(f'O maior numero é {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor numero é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}... ", end='')