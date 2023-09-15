print('===EXERCÍCIO 065===')
print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
contador = 3
print('~' * 110)
print(f'{t1} → {t2}', end='')
while contador <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' → FIM')
print('~' * 110)
