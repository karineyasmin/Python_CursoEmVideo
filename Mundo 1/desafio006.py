'''
desafio006
Enunciado

Crie um programa peça um número ao usuário e depois exiba na tela:
- O dobro do número;
- O triplo do número;
- A raíz quadrada do número. '''
#------------------------------------------------------------------------------------------------------------------------
#código
num = int(input('Digite um número: '))
                
dobro = num * 2
triplo = num * 3
raizquad = num ** (1/2)
                
print(f'\nVocê digitou o número {num} ')
print(f'\nO dobro de {num} é: {dobro}')
print(f'\nO triplo de {num} é: {triplo}')
print(f'\nA raíz quadrada de {num} é: {raizquad:.2f} ')