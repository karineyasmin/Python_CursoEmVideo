'''
desafio-038
Enunciado:

Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais '''
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Código:
print('=-' * 15)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('\nO PRIMEIRO número é o MAIOR')
elif num2 > num1:
    print('\nO SEGUNDO número é o MENOR')
elif num1 == num2:
    print('\nOs dois números são IGUAIS')
print('=-' * 15)
