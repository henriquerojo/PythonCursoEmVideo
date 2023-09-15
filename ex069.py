print('===EXERCÍCIO 069===')
contador = 0
cores = {'vermelhocomnegrito': '\033[1:31m',
         'amarelocomnegrito': '\033[1:33m',
         'limpa': '\033[m'}
while True:
    tabuada = int(input(f'Digite um número (Digite um valor {cores["vermelhocomnegrito"]}negativo{cores["limpa"]} para finalizar o programa): '))
    if tabuada < 0:
        break
    if contador <= 10:
        for contador in range(0, 11):
            print(f'{tabuada} x {contador} = {tabuada * contador}')
print(f'{cores["amarelocomnegrito"]}{"FIM DO PROGRAMA":~^75}{cores["limpa"]}')
