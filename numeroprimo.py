n = int(input('Digite um número: '))
total_divisoes = 0
pergunta = 'S'
while pergunta == 'S':
    while n <= 0:
        n = int(input('Digite um número: '))
    for c in range(1, n + 1):
        if n % c == 0:
            total_divisoes += 1
            print('\033[33m', end='')
        else:
            print('\033[31m', end='')
        print(f'{c} ', end='')
    print(f'\n\033[mO número {n} foi divisivel {total_divisoes} vezes.')
    if total_divisoes == 2:
        print('\nÉ UM NÚMERO PRIMO!')
    else:
        print('\nNÃO É PRIMO!')
    pergunta = str(input('Quer continuar?[S/N] ')).strip().upper()
    while pergunta != 'S' or pergunta != 'N':
        print('Você precisa digitar "S" ou "N".')
        pergunta = str(input('Quer continuar?[S/N] '))
    if pergunta == 'S':
        n = int(input('Digite um número: '))
