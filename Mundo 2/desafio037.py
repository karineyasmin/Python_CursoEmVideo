''' 
desafio-037
Enunciado:

Escreva um programa que leia um número qualquer e peça para o usúario escolher qual será a base de conversão:

1 - para binário
2 - para octal
3 - para hexadecimal '''
#---------------------------------------------------------------------------------------------
#código:
print('=-' * 23)
print('\tConversor de Bases Numéricas')
print('=-' * 23)

numero = int(input('Digite um número qualquer: '))
print('''\nEscolha a base de conversão:
      
      1 - para BINÁRIO
      2 - para OCTAL
      3 - para HEXADECIMAL 
      
      ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'\n{numero} convertido para binário é: {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'\n{numero} convertido para octal é: {oct(numero)[2:]}.')
elif opcao == 3:
    print(f'\n{numero} convertido para hexadecimal é: {hex(numero)[2:]}.')
else:
    print('\nOpção inválida. Escolha entre 1, 2 ou 3.')
print('=-' * 23)

