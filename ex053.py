print('===EXERCÍCIO 053===')
primeiro_termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razão = int(input('Informe a razão da progressão aritmética: '))
print(f'A progressão aritmética com 10 termos com o primeiro termo = {primeiro_termo} e a razão = {razão}, é:')
for c in range(0, 10, 1):  # início, fim, passo
    print(f'{primeiro_termo + (razão * c)}', end=' → ')
print('FIM')
