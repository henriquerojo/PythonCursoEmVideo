from time import sleep
print('===EXERCÍCIO 048===')
print('ATENÇÃO! Iremos iniciar a contagem regressiva de 10 segundos para a queima dos fogos!')
for c in range(10, -1, -1):  # início, fim, passo
    sleep(1)  # 1 segundo de espera para cada laço
    print(c)
print('KABUM!')
