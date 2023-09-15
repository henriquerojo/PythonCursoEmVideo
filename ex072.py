contador_mil_reais = soma = menor = contador = 0
barato = ''
cores = {'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'limpa': '\033[m'}
while True:
    produto = str(input('Produto: ')).strip().lower()
    preço = float(input('Preço: '))
    contador += 1
    soma += preço
    if preço > 1000.00:
        contador_mil_reais += 1
    if contador == 1:  # or preço < menor
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in 'Ss' and pergunta not in 'Nn':
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if pergunta in 'Nn':
        break
print(f'O {cores["vermelho"]}VALOR TOTAL{cores["limpa"]} da compra é de R${cores["amarelo"]}{soma:.2f}{cores["limpa"]}.')
print(f'Temos {cores["amarelo"]}{contador_mil_reais}{cores["limpa"]} produto(s) {cores["vermelho"]}ACIMA{cores["limpa"]} de R$1000.00.')
print(f'O produto mais {cores["vermelho"]}BARATO{cores["limpa"]} é o(a) {cores["amarelo"]}{barato}{cores["limpa"]} que custa R${cores["amarelo"]}{menor:.2f}{cores["limpa"]}.')
