'''Faça um programa que leia nome e peso de várias 
pessoas, guardando tudo em uma lista. No final, 
mostre quantas pessoas foram cadastradas, uma 
listagem com as pessoas mais pesadas e uma listagem 
com as pessoas mais leves.'''

temp = []
pessoas = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    pessoas.append(temp)
    temp.clear
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar [N/S]: ')).strip().upper()[0]
    if resp in "N":
        break

print('-=' * 30)
print(f'Foram cadastradas um total de {len(pessoas)}')
print('')