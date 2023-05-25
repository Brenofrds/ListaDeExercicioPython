'''Crie um programa que leia o ano de nascimento 
de sete pessoas. No final, motre quantas pessoas 
ainda não atingiram a maioridade e quantas já são 
maiores.'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for num in range(1, 8):
    nasc = int(input('Em que ano nasceu a {} pessoa nasceu: '.format(num)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e {} pessoas menores de idade'.format(totmenor))