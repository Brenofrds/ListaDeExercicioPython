'''Crie um programa que leia vários números inteiros 
pelo teclado. O programa só vai parar quando o 
usuário digitar o calor 999, que é a condição de 
parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles.'''

num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} números e a soma entre ele foi {}'.format(cont, soma))
