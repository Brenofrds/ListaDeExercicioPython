primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do progama''')
    opçao = int(input('Qual a sua opção: '))
    if opçao == 1:
        soma = primeiro + segundo
        print('A soma dos numeros é {}'.format(soma))
    elif opçao == 2:
        mult = primeiro * segundo
        print('A multiplicação dos números é {}'.format(mult))
    elif opçao == 3:
        if primeiro > segundo:
            maior = primeiro
            print('O maior número é {}'.format(maior))
        elif segundo > primeiro:
            maior = segundo
            print('O maior número é {}'.format(maior))
        elif primeiro == segundo:
            print('Os números são iguais!')
    if opçao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))


        
        

    