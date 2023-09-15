print('===EXERCÍCIO 055===')
frase = str(input('Digite uma frase: ')).strip().upper()  # tirar os espaços excessivos e deixar todas as letras maíusculas
separado = frase.split()  # separar as palavras da frase como lista
junto = ''.join(separado)  # juntar as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):  # início, fim, passo
    inverso += junto[letra]  # inverter a frase
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:  # condição composta
    print('TEMOS um PALÍNDROMO!')
else:
    print('NÃO TEMOS um PALÍNDROMO!')
