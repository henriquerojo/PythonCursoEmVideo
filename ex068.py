print('===EXERCÍCIO 068===')
contador = soma = 0
while True:
    n = int(input('Digite um número (\033[1:33mDigite 999 para parar\033[m): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} números e a soma entre eles foi de {soma}.')
