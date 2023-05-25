'''Crie um programa que vai ler vários números e 
colocar em uma lista. Depois disso, crie duas listas 
extras que vão conter apenas os valores pares e os 
valores ímpares digitados, respectivamente. Ao 
final, mostre o conteúdo das três listas geradas.'''

lista = []
pares= []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))

    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar [N/S]: ').strip().upper()[0])
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 1 == 0:
        impares.append(v)
print(f'A lista completa: {lista}')
print(f'A lista de pares: {pares}')
print(f'A lista de impares : {impares}')

