print('===EXERCÍCIO 057===')
maior = 0
menor = 0
for massa in range(1, 6):
    peso = float(input(f'Peso {massa}ª pessoa (kg): '))
    if massa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} kg.')
print(f'O menor peso lido foi de {menor} kg.')
