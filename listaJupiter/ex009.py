#9. Encontre o melhor mês (o maior lucro do ano)
receitas = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
despesas = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
tamanho = len(receitas)
Lucromaior = 0
mesMaior = ''

for c in range(0, tamanho): # 7
    lucro = receitas[c] - despesas[c]
    if lucro > Lucromaior:
        Lucromaior = lucro
        mesMaior = meses[c]

print(f'O maior lucro foi de {Lucromaior} no mês de {mesMaior}')
