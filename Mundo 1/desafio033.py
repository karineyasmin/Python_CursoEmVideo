'''
desafio033
Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor. '''
#------------------------------------------------------------------------------------------------------------------------
#código

num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('\nDigite o segundo número:\n'))
num3 = float(input('\nDigite o terceiro número:\n')) 
menor = num1

# verificando quem é o menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')