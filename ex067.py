print('===EXERCÍCIO 067===')
opção = 'S'
contador = soma = media = n = maior = menor = 0
while opção in 'Ss':
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / contador
print(f'A média dos {contador} valores que você digitou é {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
