#desafio012 
''' Crie um algortimo que leia preço de um produto e mostre seu novo preço com 5% de desconto.
'''

#CODIGO:

produto = float(input('Digite o preço do produto: '))
desconto = (produto * 5) / 100
total = produto - desconto

print(f'\nO produto custava: {produto}')
print(f'\nCom o desconto de 5% o produto custará: {total}')
