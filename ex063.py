print('===EXERCÍCIO 063===')
print(f'{"=-" * 8}{"PROGRESSÃO ARITMÉTICA"}{"-=" * 8}')
primeiro_termo = int(input('Informe o primeiro termo da progressão aritmética: '))
razão = int(input('Informe a razão da progressão aritmética: '))
contador = 1
print('')
while contador <= 10:
    print(f'{primeiro_termo} → ', end='')
    contador += 1
    primeiro_termo += razão
print('FIM')
