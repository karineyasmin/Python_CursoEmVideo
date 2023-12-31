'''
desafio-038
Enunciado:

Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais '''
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Código:
print('=-' * 40)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

if num1 > num2:
    print(f'\nO número {num1} é o maior')
elif num2 > num1:
    print(f'\nO número {num2} é o maior')
elif num1 == num2:
    print('\nNão existe valor maior. Os dois são iguais')