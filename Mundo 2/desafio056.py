'''
desafio056
Enunciado: 

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos.
'''
#------------------------------------------------------------------------------------------------
#código:
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0

for pessoa in range (1,5):
    print(f'----- {pessoa}ª Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
        
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho se chama {nomeVelho} e tem {maiorIdadeHomem} anos.')
print(f'Ao todo {totalMulher20} mulheres têm menos de 20 anos.')
