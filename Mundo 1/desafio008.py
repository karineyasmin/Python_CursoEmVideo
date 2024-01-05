'''
desafio008
Enunciado

Crie um código para ler um valor em metros e fazer a conversão em centímetros e milímetros. '''
#------------------------------------------------------------------------------------------------------------------------
#código

metros = float(input('Digite o valor em metros: '))

print(f'\nVocê digitou {metros} m') 
print(f'\n{metros} m é equivalente a {metros * 100} centímetros')
print(f'\n{metros} m é equivalente a {metros * 1000} milímetros ')