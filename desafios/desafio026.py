'''Faça um programa que leia uma frase pelo teclado e mostre:

- quantas vezes aparece a letra "A"

- em que posição ela aparece a primeira vez

- em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ' )).upper().strip()

print (f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'\nA primeira letra A apareceu na posição {frase.find("A")+1}') #+1 adequa a posição para começar no 1 inves de 0
print(f'\nA Ultima letra A apareceu na posição {frase.rfind("A")}+1')
