'''
desafio010

Crie um programa para ler quanto dinheiro a pessoa tem na carteira e mostrar quantos dólares ela pode comprar. '''
# ***dolar a 3,27***
#------------------------------------------------------------------------------------------------------------------------
#código

real = float(input('Quanto você tem quem reais? '))
dolar = real * 3.27

print(f'\nVocê tem R${real:.2f}')
print(f'\nQue equivale a ${dolar:.2f}')

