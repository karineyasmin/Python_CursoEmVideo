'''faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados.

ex: digite um numero: 1834
unidade:4
dezena:3
centena:8
milhar:1

Galera, pra ficar mais claro:
o símbolo // faz a divisão e só pega o que esta antes da vírgula.
o símbolo % faz a divisão e só pega o que esta depois da vírgula.
'''

'''num = input('Digite um número de 0 a 999: ')

unidade = num[-3]
dezena  = num[-2]
centena = num[-1]
milhar  = num[0]

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')