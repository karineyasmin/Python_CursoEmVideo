'''
desafio002
Enunciado

Crie um programa que peça para o usuário digitar algo e exiba na tela:

- O tipo primitivo
- Se é um numeral;
- Se é alfanumerico;
- Se todas as letras são maiúsculas;
- Se todas as letras são maiúsculas;
- Se ó tem espaços
- Se está captalizado. '''
#------------------------------------------------------------------------------------------------------------------------
#código

dado = input('Digite algo: ')

print(f'Qual é o tipo primitivo? {type(dado)}')   
print(f'É um número? {dado.isnumeric()}')
print(f'É alfabético? {dado.isalpha()}')
print(f'É alfanumérico? {dado.isalnum()}')                                                         
print(f'Todas as letras são maiúsculas? {dado.isupper()}')
print(f'Todas as letras são minúsculas? {dado.islower()}')
print(f'Só tem espaços? {dado.isspace()}')
print(f'Está captalizado? {dado.istitle()}')


