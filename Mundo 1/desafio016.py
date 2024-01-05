'''
desafio016

Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira. Exemplos

6.127
6
'''
#------------------------------------------------------------------------------------------------------------------------
#código

print('*' * 60)
# usando a função interna int
num = float(input('Digite um número real: '))
print(f'O número digitado foi {num:.2f} e a sua porção inteira é {int(num)}')