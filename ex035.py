from time import sleep
print('===EXERCÍCIO 035===')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))
print('Analisando qual é o maior e o menor valor, aguarde um instante...')
sleep(2)
# Verificando qual é o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor é o \033[31m{menor}\033[m')
# Verificando qual é o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é o \033[31m{maior}\033[m')
