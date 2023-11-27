'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%;
Para os inferiores ou iguais, o aumento é de 15%.'''

#CODIGO

salario = float(input('Digite o salário: '))

if salario > 1250.00:
    salario = (salario * 0.10) + salario
    print(f'Seu salário terá um aumento será de 10%.\n Seu novo salário é de {salario:.2f}')
else:
    salario = (salario * 0.15) + salario
    print(f'Seu salário terá um aumento será de 15%.\n Seu novo salário é de {salario:.2f}')
