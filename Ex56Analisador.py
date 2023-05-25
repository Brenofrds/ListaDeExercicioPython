'''Desenvolva um progama que leia o nome, idade 
e sexo de 4 pessoas. No final do programa, mostre 
a media de idade do grupo, qual é o nome do homem 
mais velho e quantas mulheres tem menos de 20 anos.'''

totalidade = 0
maioridade = 0
nomemaioridade = ''
totmulher = 0

for pessoas in range( 1, 5):
    print('------ {} pessoa ------'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    totalidade += idade
    media = totalidade / 4
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomemaioridade = nome
    if idade < 20 and sexo in 'Ff':
        totmulher += 1

print('A media da idade das pessoas é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomemaioridade))
print('E nessa lista tem {} mulheres com menos de 20 anos'.format(totmulher))