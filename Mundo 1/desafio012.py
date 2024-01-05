'''
desafio012 

Crie um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto. '''
#------------------------------------------------------------------------------------------------------------------------
#código

produto = float(input('Digite o preço do produto: '))
desconto = (produto * 5) / 100
total = produto - desconto

print(f'\nO produto custava: {produto:.2f}')
print(f'\nCom o desconto de 5% o produto custará: {total:.2f}')
