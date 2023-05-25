from datetime import date
atual = date.today().year
nasc = int(input("Em qual ano você nasceu: "))
anos = atual - nasc
if anos == 18:
    print('Você tem {} anos'.format(anos))
    print('e deve se alistar IMEDIATAMENTE')
elif anos > 18:
    print('Você tem {} anos'.format(anos))
    print('e deveria ter se alistado a {} anos atrás em {}'.format(anos - 18, nasc + 18))
elif anos < 18:
    print('Você tem {} anos'.format(anos))
    print('e deverá se alistar daqui {} anos em {}'.format(18 - anos, nasc + 18))