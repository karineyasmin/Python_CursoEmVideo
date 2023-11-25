''' crie um programa que leia um numero inteiro e msotre na tela se 
é par ou impar '''



numero = int(input('Para saber um número é par ou impar, digite um número inteiro:\n'))

if numero % 2 == 0:
    print(f'O número é par')
else:
    print('o número é ímpar')

