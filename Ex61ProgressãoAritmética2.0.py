'''Refaça o DESAFIO 51, lendo o primeiro termo e a 
razão de um PA, mostrando os 10 primeiros termos da 
progressão usando a estrutura WHILE'''

print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('FIM!!!')