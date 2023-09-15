print('===EXERCÍCIO 050===')
soma = 0  # acumulador
cont = 0  # contador
contador_ímpar = 0
for c in range(1, 501, 2):  # início, fim e passo
    contador_ímpar = contador_ímpar + 1  # contador_ímpar += 1
    if c % 3 == 0:
        soma = soma + c  # soma += c
        cont = cont + 1  # cont += 1
print(f'Entre 1 e 500 existem {contador_ímpar} números ímpares.')
print(f'Entre 1 e 500 existem {cont} valores divisíveis por 3 e ímpares')
print(f'A soma de todos os {cont} valores ímpares entre 1 e 500 divisíveis por 3 é: {soma}')
