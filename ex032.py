from time import sleep
print('===EXERCÍCIO 032===')
n = int(input('Digite um número qualquer: '))
conta = n % 2
print('\033[33mAnalisando o número...\033[m')
sleep(3)
print('{}{}{}'.format('\033[36m', n, '\033[m'))
if conta == 0:
    print(f'\033[36m{n}\033[m é um número \033[31mPAR\033[m')
else:
    print(f'\033[36m{n}\033[m é um número \033[31mÍMPAR\033[m')
