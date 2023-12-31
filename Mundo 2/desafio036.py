''' 
desafio-036 
Enunciado:

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não vai poder excer 30% do salario ou entao o empréstimo será negado '''

#--------------------------------------------------------------------------------#
#código:

print('-' * 40)
print('\nCALCULADORA DE FINANCIAMENTO IMOBILIARIO')
print('-' * 40) 

valorCasa = float(input('\nQual é o valor do imóvel? R$'))
salario = float(input('\nDigite o seu salário: R$'))
prazoAnos = int(input('\nEm quantos anos você quer pagar? '))
prazoMeses = prazoAnos * 12

porcentagemSalario = float((30 * salario) / 100) #30% do salario
valorParcela = valorCasa / prazoMeses

if porcentagemSalario > valorParcela:
    print('\nParabéns. Seu empréstimo está aprovado.')
    print(f'\nSua parcela será de R${valorParcela:.2}')
else:
    print('\nSinto muito. Seu empréstimo foi negado')
    print('A parcela excederia o limite de 30% do valor do seu salario')
print('-' * 40) 
