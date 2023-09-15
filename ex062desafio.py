print('===DESAFIO EXERCÍCIO 062===')
n = int(input('Digite um número: '))
f = 1
for fatorial in range(n, 0, -1):
    print(f'{fatorial} ', end='')
    if fatorial > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= fatorial
print(f'{f}', end='')
