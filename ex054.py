print('===EXERCÍCIO 054===')
total = 0  # contador
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1:33m ', end='')
        total = total + 1
    else:
        print('\033[31m ', end='')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível \033[36m{total}\033[m vezes.\033[m')
if total == 2:  # condição composta
    print(f'{n} é um número \033[34mPRIMO\033[m.')
else:
    print(f'{n} \033[1:31mNÃO\033[m é um número \033[34mPRIMO\033[m.')
