#desafio027

'''
Faça um programa que leia o nome completo de uma pessoa
e mostre em seguida o primeiro e o ultimo nome separadamente

ex: ana maria de souza
primeiro = ana
último = souza
'''
#CODIGO:

nome = str(input('Digite seu nome completo: ')).strip()

separado = nome.split() 

print(f'o primeiro nome é: {separado[0]}')
print(f'O último nome é: {separado[-1]}')
