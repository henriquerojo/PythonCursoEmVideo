from time import sleep
print('===EXERCÍCIO 064===')
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
total = 0
termos = 10
while termos != 0:
    total += termos  # BASICAMENTE É COMO SE O TOTAL = TERMOS = 10  # total = total + termos
    while contador <= total:
        print(f'{primeiro_termo} → ', end='')
        primeiro_termo += razão  # primeiro_termo = primeiro_termo + 1
        contador += 1  # contador = contador + 1
    print('PAUSA')
    termos = int(input('Quantos termos deseja adicionar? '))  # ELE SOMA O TANTO DE TERMOS QUE VOCÊ INSERIR AQUI, ELE JA COMEÇA COM 10
print('Aguarde...')
sleep(1)
print(f'Fim do programa de progressão aritmética (PA)!\nFoi analisado um total de {total} termos!')
