''' 
desafio-036 
Enunciado:

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

#--------------------------------------------------------------------------------#
#código:

print('-' * 40)
print('\nCALCULADORA DE FINANCIAMENTO IMOBILIARIO')
print('-' * 40) 

valorCasa = float(input('\nQual é o valor do imóvel? R$'))
salario = float(input('\nQual o salário do comprador? R$'))
prazoAnos = int(input('\nQuantos anos de financiamento? '))
prazoMeses = prazoAnos * 12
porcentagemSalario = float((30 * salario) / 100) #30% do salario
valorParcela = valorCasa / prazoMeses
print('-' * 40) 
if porcentagemSalario >= valorParcela:
    print('\nEmpréstimo pode ser aprovado.')
    print(f'\nA parcela será de R${valorParcela:.2f}')
else:
    print('\nO empréstimo foi negado')
    print(f'A parcela seria de R${valorParcela:.2f}.')
    print('Ela excederia o limite de 30% do valor do salário.')
print('-' * 40) 
