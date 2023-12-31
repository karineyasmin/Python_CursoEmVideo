''' 
desafio-042 
Enunciado:

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todas os lados iguais;
- Isósceles: dois lados iguais;
- Escoleno: todos os lados diferentes; '''
#----------------------------------------------------------------------------------------------------------------------
#código:

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
