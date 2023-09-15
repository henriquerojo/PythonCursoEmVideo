print('===EXERCÍCIO 025===')
num = int(input('Digite um número entre 0 e 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número \033[32m{num}\033[m')
print(f'Unidade: \033[36m{u}\033[m')
print(f'Dezena: \033[36m{d}\033[m')
print(f'Centena: \033[36m{c}\033[m')
print(f'Milhar: \033[36m{m}\033[m')
