'''Melhore o desafio 61, perguntando para o usuário 
se ele quer mostrar mais alguns termos. O programa 
encerra quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))