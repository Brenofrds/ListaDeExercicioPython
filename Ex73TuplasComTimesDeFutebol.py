'''Crie uma tupla preenchida com os 20 primeiros 
colocados da tabela do campeonato brasileiro de 
futebol, na ordem de colocação, Depois mostre, os 
5 primeiros, os ultimos 4 colocados, times em ordem 
alfabetica e em que posilçao está o time da 
chapecoense.'''

times = ('Corinthians', 'Palmeiras', 'Santos', 
         'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 
         'Chapecoense', 'Atlético', 'Botafogo', 
         'Atlético-PR', 'Bahia', 'São Paulo', 
         'Fluminense', 'Sport Recife', 'EC Vitória', 
         'Coritiba', 'Avaí', 'Ponte Preta', 
         'Atlético-GO') 
print('-=' * 25)
print(f'Lista de times do brasileião: {times}')
print('-=' * 25)
print(f'Os 5 priemiros são: {times [0:5]}')
print('-=' * 25)
print(f'Os últimos 4 colocados: {times[-4:]}')
print('-=' * 25)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 25)
print(f'O chapecoense está na {times.index("Chapecoense")+1} posição')