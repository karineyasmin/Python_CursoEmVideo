'''
desafio019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e exibindo o nome do escolhido. '''
#------------------------------------------------------------------------------------------------------------------------
#código

from random import choice

aluno1 = input(str('Digite o nome do aluno(a): '))
aluno2 = input(str('Digite o nome do aluno(a): '))
aluno3 = input(str('Digite o nome do aluno(a): '))
aluno4 = input(str('Digite o nome do aluno(a): '))

lista = [aluno1,aluno2, aluno3, aluno4] 
escolhido = choice(lista)

print(f'O aluno sorteado foi: {escolhido}')