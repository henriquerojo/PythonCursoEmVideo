"""from math import factorial
from time import sleep
print('===EXERCÍCIO 062===')
n = int(input('Informe um número: '))
print('Aguarde...')
sleep(1)
print(f'O fatorial de {n} é igual a: {factorial(n)}')"""
#  from time import sleep
print('===EXERCÍCIO 062===')
n = int(input('Digite um número para calcular seu fatorial: '))  # número
c = n  # contador
f = 1  # "multiplicação limpa"  # fatorial
print('Aguarde...')
#  sleep (1)
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print(f'{f}', end='')
