'''Crie um programa que vai ler vários números e 
colocar em uma lista. Depois disso, mostre: quantos 
números foram digitas, a lista de valores ordenada 
de forma decrescente e se o valor 5 foi digitado e 
eatá ou não na lista.'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    if resp in "N":
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encotrado a lista')
    
