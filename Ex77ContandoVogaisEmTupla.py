'''Crie um programa que tenha uma tupla com várias 
palavras(não usar acentos). Depois disso, você deve 
mostrar, para cada palavra, quais as suas vogais. '''

palavras = ('aprender', 'programar', 'liguagem', 
            'python', 'curso', 'gratis', 'estudar', 
            'praticar', 'trabalhar', 'mercado', 
            'pragramador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra}', end=' ')