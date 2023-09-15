cont_impar = 0
n = 0
while True:
    if n % 2 == 1:
        print('\033[31m')
        cont_impar += 1
    else:
        print('\033[m')
    print(n, end='')
    n += 1
    if n == 250:
        break
print(f'\n\033[mO número de números ímpares de 0 até 250 é {cont_impar}')
