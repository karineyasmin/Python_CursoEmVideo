'''
desafio-040
Enunciado:

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO;
- Média entre 5.0 e 6.9: RECUPERAÇÃO;
- Média 7.0 ou superior: APROVADO; '''
#------------------------------------------------------------------------------------------------------------
#código:
print('=-' * 20)
print('\tCalculadora de notas')  
print('=-' * 20)    
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f'\nSua média é {media} \nVocê está APROVADO')
elif media > 5.0:
    print(f'\nSua média é {media} \nVocê está em RECUPERAÇÃO')
else: 
    print(f'\nSua média é {media} \nVocê está REPROVADO!')
print('=-' * 20)