casa = float(input('Qual o valor da casa: '))
ano = int(input("Quantos anos para pagar a casa: "))
salario = float(input('Qual é o seu salario: '))
prestação = casa / (ano * 12)
minimosalario = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if minimosalario >= prestação:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')
