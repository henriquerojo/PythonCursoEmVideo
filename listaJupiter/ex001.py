# 1. Escreva um programa que calcule a soma de todos os números pares de 1 a 100 e imprima o resultado.
soma = 0
for i in range(2, 101, 2):
    soma += i
print(f'A soma de todos os números pares entre 1 e 100 é de {soma}')
