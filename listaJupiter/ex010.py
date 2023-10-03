# 10. Escreva um programa que verifique se uma frase inserida pelo usuário é um palíndromo.
# Um palíndromo é uma frase que pode ser lida da mesma forma da esquerda para a direita e vice-versa.
frase = str(input('Digite uma frase: ')).strip().upper()  # tirar os espaços excessivos e deixar todas as letras maíusculas
separado = frase.split()  # separar as palavras da frase como lista
junto = ''.join(separado)  # juntar as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]  # inverter a frase
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('TEMOS um PALÍNDROMO!')
else:
    print('NÃO TEMOS um PALÍNDROMO!')
