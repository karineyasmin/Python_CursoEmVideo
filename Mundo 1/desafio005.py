'''
desafio005
Enunciado

Crie um programa que peça um número ao usuário e exiba na tela o seu antecessor e sucessor. '''
#------------------------------------------------------------------------------------------------------------------------
#código

num = int(input('Digite um número: '))

print(f'\nVocê digitou o número {num}')
print(f'\nSeu antecessor é {num - 1}')
print(f'Seu sucessor é {num + 1}')
