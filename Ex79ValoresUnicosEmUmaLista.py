lista = list()
resp = ''
while True:

    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso!!')
    else:
        print('Esse número já estar na lista')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    if resp in 'Nn':
        break
            
lista.sort()
print(f'Você digitou os valores {lista}')