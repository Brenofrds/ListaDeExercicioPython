'''Crie um programa que tenha uma tupla totamente 
preenchida com uma contagem por extenso, de zero 
até vinte. Seu progrma deverá ler um número pelo 
teclado (entre 0 e 20) e mostrá-lo por externso.'''

numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
           'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o número {numeros[num]}')


