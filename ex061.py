from time import sleep
print('\033[35m===EXERCÍCIO 061===\033[m')
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'vermelhonegrito': '\033[1:31m',
         'verdenegrito': '\033[1:32m',
         'limpa': '\033[m'}
soma = 0
multiplicar = 0
opção = 0
print(f'{cores["amarelo"]}={cores["limpa"]}' * 20)
n1 = int(input(f'{cores["azul"]}Primeiro número{cores["limpa"]}: '))
n2 = int(input(f'{cores["azul"]}Segundo número{cores["limpa"]}: '))
print(f'{cores["amarelo"]}={cores["limpa"]}' * 20)
while opção != 5:
    print(f"""
    {cores["verde"]}[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa{cores["limpa"]}
    """)
    print(f'{cores["amarelo"]}={cores["limpa"]}' * 21)
    opção = int(input(f'{cores["azul"]}Qual é a sua opção?{cores["limpa"]} '))
    print(f'{cores["amarelo"]}={cores["limpa"]}' * 21)
    if opção == 1:
        print('Aguarde...')
        sleep(1)
        soma = n1 + n2
        print('')
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 30)
        print(f'A soma de {cores["ciano"]}{n1}{cores["limpa"]} + {cores["ciano"]}{n2}{cores["limpa"]} é igual a: {cores["verdenegrito"]}{soma}{cores["limpa"]}')
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 30)
        print('')
    elif opção == 2:
        print('Aguarde...')
        sleep(1)
        multiplicar = n1 * n2
        print('')
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 40)
        print(f'A multiplicação de {cores["ciano"]}{n1}{cores["limpa"]} x {cores["ciano"]}{n2}{cores["limpa"]} é igual a: {cores["verdenegrito"]}{n1 * n2}{cores["limpa"]}')
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 40)
        print('')
    elif opção == 3:
        if n1 > n2:
            print('Aguarde...')
            sleep(1)
            print('')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 64)
            print(f'Analisando os valores {cores["ciano"]}{n1}{cores["limpa"]} e {cores["ciano"]}{n2}{cores["limpa"]}, verificamos que {cores["verde"]}{n1}{cores["limpa"]} é {cores["vermelho"]}MAIOR{cores["limpa"]} que {cores["cinza"]}{n2}{cores["limpa"]}.')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 64)
            print('')
        elif n2 > n1:
            print('Aguarde...')
            sleep(1)
            print('')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 64)
            print(f'Analisando os valores {cores["ciano"]}{n1}{cores["limpa"]} e {cores["ciano"]}{n2}{cores["limpa"]}, verificamos que {cores["verde"]}{n2}{cores["limpa"]} é {cores["vermelho"]}MAIOR{cores["limpa"]} que {cores["cinza"]}{n1}{cores["limpa"]}.')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 64)
            print('')
        elif n1 == n2:
            print('Aguarde...')
            sleep(1)
            print('')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 68)
            print(f'Analisando os valores {cores["ciano"]}{n1}{cores["limpa"]} e {cores["ciano"]}{n2}{cores["limpa"]}, verificamos que os valores são {cores["vermelho"]}IGUAIS{cores["limpa"]}.')
            print(f'{cores["amarelo"]}={cores["limpa"]}' * 68)
            print('')
    elif opção == 4:
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 21)
        n1 = int(input(f'{cores["azul"]}Primeiro número{cores["limpa"]}: '))
        n2 = int(input(f'{cores["azul"]}Segundo número{cores["limpa"]}: '))
        print(f'{cores["amarelo"]}={cores["limpa"]}' * 21)
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa!')
    else:
        print(f'{cores["vermelhonegrito"]}Opção inválida{cores["limpa"]}. Por favor, tente novamente!')
