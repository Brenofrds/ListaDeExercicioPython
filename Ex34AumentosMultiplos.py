salario = float(input('Qual o salario do funcionario?'))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print('Quem ganhava RS{:.2f} passa a ganhar RS{:.2f} agora'.format(salario, novosalario))
