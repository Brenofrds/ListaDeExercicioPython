print('{:=^40}'.format(' Lojas Guanabara '))
preco = float(input('Qual o preço da conta: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] Em até duas vezes no cartão
[ 4 ] 3x ou mais vezes no cartão''')
opcao = int(input('Qual a sua opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total =  preco + (preco * 20 / 100)
    totalparcela = int(input('Quantas parcelas: '))
    parcela = preco / totalparcela
    print('Sua conta será parcela em {}x de R${:.2f} com juros'.format(totalparcela, parcela))
else:
    total = preco
    print('Opção INVALIDA, por favor tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))