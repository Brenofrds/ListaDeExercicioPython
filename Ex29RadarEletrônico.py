velocidade = float(input('Qual a sua velocidade atual do carro: '))
if velocidade > 80:
    print("Multado, vc passou do limite de velocidade")
    multa = (velocidade-80) * 7
    print("E agora deve pagar uma multa de {:.2f} R$".format(multa))
else:
    print("Parabens, continue dirigindo com segurança")