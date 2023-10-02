# 2. Escreva um programa que solicite ao usuário um número inteiro positivo e calcule o fatorial desse número.
# Em seguida, imprima o resultado. (Loop for)
n = int(input('Digite um número inteiro positivo: '))
for c in range(n - 1, 0, -1):
    n = n * c
print(n)
