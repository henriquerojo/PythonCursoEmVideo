#7. Encontre os meses bons (aqueles em que o lucro foi 50% maior do que a média mensal) e os coloque dentro de uma lista.

receitas = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
despesas = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

acumulador = 0
tamanho = len(receitas)
mesesLucroMaior = []
contador = 1

for c in range(0, tamanho):
    lucro = receitas[c] - despesas[c]
    acumulador += lucro
media = acumulador / 12

#definindo 50% de media
percentual = (media * 50) / 100

for c in range(0, tamanho):
    lucro = receitas[c] - despesas[c]
    if lucro > (media + percentual):
        mesesLucroMaior.append(meses[c])
print(mesesLucroMaior)
