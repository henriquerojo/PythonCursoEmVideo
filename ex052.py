print('===EXERCÍCIO 052===')
soma = 0  # acumulador
contador = 0  # contador
for c in range(1, 7):  # início, fim
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'Você informou {contador} número(s) par(es). Realizando a soma entre os valores par(es) seu resultado é: {soma}')
