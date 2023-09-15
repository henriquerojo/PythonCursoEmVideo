from time import sleep
print('===EXERCÍCIO 066===')
contador = 0  # contador = soma = subtração = n = 0
soma = 0
subtração = 0
n = 0
while n != 999:
    n = int(input('Digite um número [\033[1:33mDigite 999 para parar\033[m]: '))
    soma += n
    contador += 1
    if n == 999:
        subtração = soma - 999
        print('Finalizando...')
sleep(1)
print(f'Código finalizado! A soma dos {contador - 1} valores digitados é de {subtração}.')
